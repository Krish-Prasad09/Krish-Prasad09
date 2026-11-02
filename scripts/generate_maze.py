import json
import os
import random
import sys
import urllib.request
from collections import deque

USER = os.environ.get("GH_USER", "Krish-Prasad09")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = os.environ.get("MAZE_OUT", "assets/github-maze.svg")
DEMO = "--demo" in sys.argv

LEVELS = ["#161b22", "#0c2d6b", "#1158c7", "#388bfd", "#79c0ff"]
WALL = "#484f58"
CELL = 16
PAD = 24
TOP = 44
BOTTOM = 28

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { contributionCount weekday } }
      }
    }
  }
}
"""


def fetch_calendar():
    body = json.dumps({"query": QUERY, "variables": {"login": USER}}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    cal = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    weeks = []
    for w in cal["weeks"]:
        col = [0] * 7
        for d in w["contributionDays"]:
            col[d["weekday"]] = d["contributionCount"]
        weeks.append(col)
    return weeks, cal["totalContributions"]


def demo_calendar():
    rnd = random.Random(7)
    weeks = [[rnd.choice([0, 0, 0, 1, 2, 3, 5, 8, 12]) for _ in range(7)] for _ in range(53)]
    return weeks, sum(sum(w) for w in weeks)


def level_fn(weeks):
    vals = sorted(v for w in weeks for v in w if v > 0)
    if not vals:
        return lambda v: 0
    q = [vals[int(len(vals) * p)] for p in (0.25, 0.5, 0.75)]

    def f(v):
        if v == 0:
            return 0
        if v <= q[0]:
            return 1
        if v <= q[1]:
            return 2
        if v <= q[2]:
            return 3
        return 4

    return f


def build_maze(cols, rows, seed):
    rnd = random.Random(seed)
    open_ = {(c, r): set() for c in range(cols) for r in range(rows)}
    seen = {(0, 0)}
    stack = [(0, 0)]
    while stack:
        c, r = stack[-1]
        nbrs = [
            (c + dc, r + dr)
            for dc, dr in ((1, 0), (-1, 0), (0, 1), (0, -1))
            if 0 <= c + dc < cols and 0 <= r + dr < rows and (c + dc, r + dr) not in seen
        ]
        if not nbrs:
            stack.pop()
            continue
        n = rnd.choice(nbrs)
        open_[(c, r)].add(n)
        open_[n].add((c, r))
        seen.add(n)
        stack.append(n)
    return open_


def solve(open_, start, goal):
    prev = {start: None}
    q = deque([start])
    while q:
        cur = q.popleft()
        if cur == goal:
            break
        for n in open_[cur]:
            if n not in prev:
                prev[n] = cur
                q.append(n)
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    return path[::-1]


def render(weeks, total):
    cols, rows = len(weeks), 7
    lvl = level_fn(weeks)
    open_ = build_maze(cols, rows, f"{USER}-{cols}")
    path = solve(open_, (0, 0), (cols - 1, rows - 1))
    w = PAD * 2 + cols * CELL
    h = TOP + rows * CELL + BOTTOM
    ox, oy = PAD, TOP
    parts = []
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
    )
    parts.append(
        "<style>"
        ".t{font:600 12px 'SFMono-Regular',Consolas,monospace;fill:#8b949e}"
        ".p{fill:none;stroke:#f0f6fc;stroke-width:3;stroke-linecap:round;stroke-linejoin:round;"
        "stroke-dasharray:var(--l);stroke-dashoffset:var(--l);animation:run 9s ease-in-out infinite}"
        ".g{fill:none;stroke:#58a6ff;stroke-width:7;stroke-linecap:round;stroke-linejoin:round;opacity:.35;"
        "stroke-dasharray:var(--l);stroke-dashoffset:var(--l);animation:run 9s ease-in-out infinite}"
        "@keyframes run{0%{stroke-dashoffset:var(--l);opacity:1}65%{stroke-dashoffset:0;opacity:1}"
        "90%{stroke-dashoffset:0;opacity:1}100%{stroke-dashoffset:0;opacity:0}}"
        "</style>"
    )
    parts.append(f'<rect width="{w}" height="{h}" rx="10" fill="#0d1117"/>')
    parts.append(f'<text class="t" x="{PAD}" y="26">{USER} / contribution maze</text>')
    parts.append(
        f'<text class="t" x="{w - PAD}" y="26" text-anchor="end">{total} contributions in the last year</text>'
    )
    for c in range(cols):
        for r in range(rows):
            parts.append(
                f'<rect x="{ox + c * CELL}" y="{oy + r * CELL}" width="{CELL}" height="{CELL}" fill="{LEVELS[lvl(weeks[c][r])]}"/>'
            )
    walls = []
    for c in range(cols):
        for r in range(rows):
            x, y = ox + c * CELL, oy + r * CELL
            if (c + 1, r) not in open_[(c, r)]:
                walls.append(f"M{x + CELL} {y}V{y + CELL}")
            if (c, r + 1) not in open_[(c, r)]:
                walls.append(f"M{x} {y + CELL}H{x + CELL}")
    walls.append(f"M{ox} {oy}H{ox + cols * CELL}")
    walls.append(f"M{ox} {oy}V{oy + rows * CELL}")
    walls.append(f"M{ox + cols * CELL} {oy}V{oy + rows * CELL}")
    walls.append(f"M{ox} {oy + rows * CELL}H{ox + cols * CELL}")
    parts.append(
        f'<path d="{"".join(walls)}" stroke="{WALL}" stroke-width="1.6" fill="none" stroke-linecap="square"/>'
    )
    pts = [(ox + c * CELL + CELL / 2, oy + r * CELL + CELL / 2) for c, r in path]
    d = "M" + "L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    length = int(sum(abs(pts[i][0] - pts[i - 1][0]) + abs(pts[i][1] - pts[i - 1][1]) for i in range(1, len(pts)))) + 2
    parts.append(f'<path class="g" style="--l:{length}" d="{d}"/>')
    parts.append(f'<path class="p" style="--l:{length}" d="{d}"/>')
    parts.append(f'<circle cx="{pts[0][0]:.1f}" cy="{pts[0][1]:.1f}" r="4" fill="#3fb950"/>')
    parts.append(f'<circle cx="{pts[-1][0]:.1f}" cy="{pts[-1][1]:.1f}" r="4" fill="#f85149"/>')
    lx = w - PAD - 5 * 12 - 60
    ly = TOP + rows * CELL + 18
    parts.append(f'<text class="t" x="{lx}" y="{ly}" text-anchor="end">Less</text>')
    for i, col in enumerate(LEVELS):
        parts.append(f'<rect x="{lx + 8 + i * 12}" y="{ly - 10}" width="10" height="10" rx="2" fill="{col}"/>')
    parts.append(f'<text class="t" x="{lx + 8 + 5 * 12 + 4}" y="{ly}">More</text>')
    parts.append("</svg>")
    return "".join(parts)


def main():
    weeks, total = demo_calendar() if DEMO else fetch_calendar()
    svg = render(weeks, total)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        f.write(svg)


main()

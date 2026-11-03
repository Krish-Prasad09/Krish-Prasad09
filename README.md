<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1f6feb,100:58a6ff&height=200&section=header&text=Krish%20Prasad&fontSize=58&fontColor=ffffff&fontAlignY=40&animation=fadeIn&desc=B.Tech%20EE%20%40%20IIT%20Indore&descSize=20&descAlignY=62" alt="header" width="100%" />

<img src="https://raw.githubusercontent.com/Krish-Prasad09/Krish-Prasad09/main/assets/ascii-portrait.svg?v=1" alt="Krish Prasad ASCII portrait" width="560" />

<br/><br/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=58A6FF&center=true&vCenter=true&width=650&lines=B.Tech+Electrical+Engineering+%40+IIT+Indore;Full-Stack+Developer+%7C+ML%2FAI+Enthusiast;Building+with+React%2C+Node.js+%26+PyTorch;Member%2C+Quantum+Computing+Club+%40+IIT+Indore" alt="Typing SVG" />

<br/>

<img src="https://raw.githubusercontent.com/Krish-Prasad09/Krish-Prasad09/main/assets/github-maze.svg" alt="GitHub contribution maze" width="100%" />

<br/>

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://portfolio-eta-drab-22.vercel.app/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/krish-prasad-29469633b/)
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/krish_ji/)
[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-2F8D46?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/profile/kpji?tab=activity)
[![CodeChef](https://img.shields.io/badge/CodeChef-5B4638?style=for-the-badge&logo=codechef&logoColor=white)](https://www.codechef.com/users/krizzh)
[![Codeforces](https://img.shields.io/badge/Codeforces-1F8ACB?style=for-the-badge&logo=codeforces&logoColor=white)](https://codeforces.com/profile/Krizzh9306)

</div>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:1f6feb,100:58a6ff&height=2&section=header" width="100%" alt="divider" />

## 🚀 About Me

- 🎓 B.Tech in **Electrical Engineering** at **IIT Indore**
- 💻 Focused on **full-stack web development** and **applied ML**, building tools to solve real-world problems using technology.
- 🧩 Active on [**LeetCode**](https://leetcode.com/u/krish_ji/), [**GeeksforGeeks**](https://www.geeksforgeeks.org/profile/kpji?tab=activity), [**CodeChef**](https://www.codechef.com/users/krizzh), and [**Codeforces**](https://codeforces.com/profile/Krizzh9306), sharpening DSA and problem-solving
- 🛠️ Currently polishing projects and resume for upcoming internship opportunities.

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:1f6feb,100:58a6ff&height=2&section=header" width="100%" alt="divider" />

## 🌟 Featured Projects



<br/>

### 📈 [Self-Learning PMS/AIF Statement Parser](https://github.com/Krish-Prasad09/StatementParser)
*Problem Statement of a Fintech Company*

An autonomous financial statement ingestion and multi-custodian portfolio consolidation engine for **SEBI-registered PMS and AIF funds**. Solves the multi-format wealth data fragmentation problem by combining **one-shot LLM template synthesis** with **sub-50ms deterministic Python execution**, eliminating ongoing AI token costs and hallucination risks.

**Key Highlights:**
- ⚡ **One-Shot Learning Architecture:** Leverages **Gemini API** once on unseen statement layouts to synthesize declarative JSON parsing schemas, executing deterministic **sub-50ms parsing** with **zero AI calls** thereafter across **30+ statement formats** (PDF, multi-sheet Excel, and sectioned CSV).

- 🛡️ **17-Rule Financial Safety Gate:** Enforces double-entry roll-forward reconciliations, row-level arithmetic (`Quantity * Price == Market Value`), and **ISO 6166 Mod-10 Luhn checksum verification** on stock ISINs to strictly fail closed against data corruption.

- 💼 **Multi-Custodian Portfolio Consolidator:** Unifies client wealth across fragmented wealth managers (Kotak, ASK, ICICI) joined by **12-character ISIN** and **PAN**, with absolute **INR/USD currency isolation** and dedicated unlisted AIF alternative buckets.

- 🔄 **Layout Drift Interception:** Automatically flags modified table geometries or renamed columns, creates candidate `_v2` schemas with `approved: false`, and locks statements in a **Quarantine Review Queue** awaiting one-click human auditor sign-off.

- 📬 **Automated Mailbox Ingestion & Security:** Integrates an **IMAP SSL** email poller with `BODY.PEEK` idempotency to pre-classify statements from factsheets/invoices, featuring ephemeral in-memory decryption for password-locked PDFs and **Neon Cloud PostgreSQL** persistence.

`Python 3.11` `Gemini API` `Streamlit` `Neon PostgreSQL` `Pydantic v2` `pdfplumber` `openpyxl` `IMAP SSL` `Pandas` `Docker`
🔗[Video Demo](https://drive.google.com/file/d/1iaSl2R2ejnGPGycQRoGFrllXRsy7RDth/view?usp=drive_link).

<br/>

<br/>

### 🎤 [EmoSense — AI Interview Analyser & Multimodal Speech Coach](https://github.com/Krish-Prasad09/EmoSense-Interview-Analyser)
*Machine Learning in Signal Processing Course Project · Under Dr. Vivek Kanhagad, IIT Indore (Feb–Apr 2026)*

An AI-powered interview communication and vocal delivery coach that evaluates **how** a candidate speaks, not just what they say. Ingests microphone audio or uploaded files, performing dual-stream acoustic and linguistic evaluation with zero database overhead.

**Key Highlights:**
- 🎯 **Acoustic Emotion Recognition (Wav2Vec2):** Fine-tuned `facebook/wav2vec2-base` on the **CREMA-D dataset** (7,442 clips, 91 actors) across 6 emotion classes, achieving **80% test accuracy** — nearly doubling the **43% baseline** of traditional LSTM models.

- 🧠 **Multimodal Late-Fusion Architecture:** Ensembles acoustic prosody from **Wav2Vec2** with semantic sentiment from **DistilRoBERTa** on the transcribed text, eliminating false vocal tone classifications through dual-modality probability averaging.

- ⏱️ **Active-Speaking Pace & Linguistic Engine:** Leverages **OpenAI Whisper** chunk timestamps to compute delivery pace (WPM) strictly across active speech segments (excluding silences & interviewer turns), paired with multi-pass filler word detection, spoken grammar validation, and length-normalized CTTR vocabulary scoring.

- 📊 **Temporal Emotion Timeline & Canvas Visualizer:** Generates an emotion evolution timeline using a 4-second sliding window sampled every 10 seconds, rendered dynamically via an interactive, zero-dependency **HTML5 Canvas** stacked-bar visualizer.

- 🛠️ **In-Memory Audio Transcoding & Cloud Deployment:** Built a resilient **FFmpeg + Torchaudio** bridge resolving browser WebM/Opus codec limitations to 16 kHz Mono PCM WAV; containerized with **Docker** and deployed on **Hugging Face Spaces** with weights hosted on the **Hugging Face Hub**.

`Python 3.10` `Flask` `PyTorch` `Torchaudio` `Wav2Vec2` `OpenAI Whisper` `DistilRoBERTa` `Transformers` `Docker` `FFmpeg` `HTML5 Canvas`  
🔗 [Live Demo](https://huggingface.co/spaces/Krizzh/EmoSense-Interview-Analyser) 

<br/>

<br/>

### 🎓 [RankUp — Smart AI Learning Assistant & Multiplayer Study Arena](https://rank-up-learning-assistant.vercel.app/)

A full-stack **MERN** academic platform that transforms dense study notes into interactive learning tools and real-time multiplayer battles. Features in-memory streaming text parsing that supports **150+ page PDFs** with zero database bloat (>95% storage reduction).

**Key Highlights:**
- ⚡ **High-Capacity AI Study Tools:** Generates structured summaries, active-recall flashcard decks, and contextual Q&A chat (supporting document-only vs. web-grounded modes).

- 🎮 **Live Multiplayer Quiz Arena:** Built with **Socket.io** for real-time competitive study battles featuring server-authoritative countdowns, instant host controls, and live dynamic leaderboards.

- 📂 **Cross-Folder Quiz Engine:** Synthesizes custom exams across multiple document folders, paired with an AI diagnostic engine that analyzes concept gaps from incorrect answers.

- 🖨️ **Vector PDF Exports & 3D WebGL:** Generates downloadable, print-ready study sheets with **PDFKit** and features interactive **Three.js** 3D planet visualizations.

- 📅 **Gamified Productivity:** Color-coded study task calendar, daily learning streak tracking, and secure **Google OAuth 2.0 + JWT** sessions.

`React` `Vite` `Tailwind CSS` `Node.js` `Express` `MongoDB Atlas` `Socket.io` `Three.js` `Groq API` `PDFKit` `Google OAuth 2.0` `JWT`
🔗 [Live Demo](https://rank-up-learning-assistant.vercel.app/) 

<br/>

<br/>

### 🤖 [HireU — Career Assistant](https://github.com/Krish-Prasad09/HireU-CareerAssistant)
A full-stack AI career platform with a TypeScript + React.js frontend and Node.js/Express.js backend, supporting resume analysis, job-role matching, and AI-generated interview question sets. Uses the Gemini API with role-aware prompt templates for personalised career insights, ATS-optimised resume suggestions, and an **IIT-style** LaTeX resume builder. Implements Google OAuth 2.0 + JWT session management with role-based access, with Razorpay wired in for premium subscriptions. Frontend deployed on Vercel, backend on Render.

`React 19` `TypeScript` `Vite` `Tailwind CSS v4` `Node.js` `Express 5` `MongoDB Atlas` `Google OAuth 2.0` `JWT` `Gemini API` `Razorpay` · 🔗 [Live App](https://hire-u-career-assistant.vercel.app)

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:1f6feb,100:58a6ff&height=2&section=header" width="100%" alt="divider" />

<br/>

## 🧩 Other Projects

| Project | Description | Stack |
|---|---|---|
| [IITISOC-AmpaNova](https://github.com/Krish-Prasad09/IITISOC-AmpaNova) | Mixed-signal function generator & analog signal-processing system — filtering, modulation, differential equation solver circuits, and ADC↔DAC interfacing, simulated in LTspice | `LTspice` `Analog Circuit Design` |
| [JavaScript-Practice-Projects](https://github.com/Krish-Prasad09/JavaScript-Practice-Projects) | Tic-Tac-Toe, Rock-Paper-Scissors, and a live-rate Currency Converter, each deployed on Netlify | `HTML` `CSS` `JavaScript` |
| [Frontend-Practice-Projects](https://github.com/Krish-Prasad09/Frontend-Practice-Projects) | Weather App, To-Do List, Quiz App, Quote Generator, Notes App, and Age Calculator, each deployed on Netlify | `HTML` `CSS` `JavaScript` |

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:1f6feb,100:58a6ff&height=2&section=header" width="100%" alt="divider" />

## 🧠 DSA Stats

<div align="center">

<a href="https://leetcode.com/u/krish_ji/"><img src="https://leetcard.jacoblin.cool/krish_ji?theme=dark&font=Karma&ext=heatmap" alt="LeetCode Stats" /></a>

<a href="https://www.codechef.com/users/krizzh"><img src="https://img.shields.io/badge/CodeChef-krizzh-5B4638?style=for-the-badge&logo=codechef&logoColor=white" alt="CodeChef" /></a>

<a href="https://codeforces.com/profile/Krizzh9306"><img src="https://codeforces-readme-stats.vercel.app/api/card?username=Krizzh9306" alt="Codeforces Stats" /></a>

<a href="https://www.geeksforgeeks.org/profile/kpji?tab=activity">
<img src="https://img.shields.io/badge/GFG_Coding_Score-803-2F8D46?style=for-the-badge&logo=geeksforgeeks&logoColor=white" alt="GFG Coding Score" />
<img src="https://img.shields.io/badge/Problems_Solved-197-2F8D46?style=for-the-badge&logo=geeksforgeeks&logoColor=white" alt="GFG Problems Solved" />
</a>

</div>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:1f6feb,100:58a6ff&height=2&section=header" width="100%" alt="divider" />

## 🛠️ Tech Stack

<div align="center">

**Languages**

![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)

**Frontend & UI**

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

**Backend & Databases**

![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white)
![Express](https://img.shields.io/badge/Express-000000?style=for-the-badge&logo=express&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![Socket.io](https://img.shields.io/badge/Socket.io-010101?style=for-the-badge&logo=socket.io&logoColor=white)

**AI, Data Science & Machine Learning**

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

**DevOps & Tools**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

</div>

<br/>

<div align="center">

📫 Reach me on [LinkedIn](https://www.linkedin.com/in/krish-prasad-29469633b/)

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:58a6ff,50:1f6feb,100:0d1117&height=120&section=footer" width="100%" alt="footer" />

</div>

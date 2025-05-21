# 🤖 Closer Copilot

AI-powered sales call debrief assistant for high-ticket closers.

**Closer Copilot** helps you break down your sales calls, spot weak points, and improve your close rate — all by uploading a simple transcript. It’s built for serious closers who want to level up without guesswork.

---

## 🔍 What It Does

Upload a transcript (Zoom, Google Meet, Aircall, etc.) and get an instant AI-generated report showing:

- 🔑 Objections raised and how you handled them
- 🗣 Talk time balance (rep vs prospect)
- 🚫 Missed CTAs or weak closes
- 🧠 Suggestions to improve framing and objection handling
- 📄 Full call summary with timestamps and insights

This is **not** just a summarizer — it's a purpose-built assistant to help you close smarter.

---

## ⚙️ Tech Stack

- Python 3.11+
- Streamlit (UI)
- OpenAI GPT-4o (analysis)
- Whisper / Deepgram (coming soon for audio → transcript)

---

## 📁 Project Structure

closer_copilot/
│
├── app.py # Streamlit UI
├── analyzer.py # LLM prompt + parsing logic
├── utils.py # Transcript cleaning, helpers
├── prompts/
│ └── base_prompt.txt # Instruction prompt for GPT
├── examples/
│ └── sample_transcript.txt
├── outputs/
│ └── report_2025-05-20.md
├── requirements.txt
└── README.md


## 🚧 Roadmap

- [x] Upload `.txt` transcript
- [x] Analyze with GPT-4o
- [ ] Add Whisper audio transcription
- [ ] Store multiple call reports per user
- [ ] Add CRM (Close.com, HubSpot) context
- [ ] Build real-time live coaching Copilot

---

## 🧠 Why I'm Building This

As a former high-ticket closer, I always wished there was a tool that gave me **honest feedback** on my sales calls without needing a manager.  
Now I’m building that tool — first for myself, then for every closer who wants to get sharper.

---

## 🚀 Get Started

git clone https://github.com/yourusername/closer_copilot.git
cd closer_copilot
pip install -r requirements.txt
streamlit run app.py







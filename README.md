# MindEase 🧠

<div align="center">

**AI-powered mental health support chatbot — RAG pipeline, crisis detection, compassionate responses**

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq_AI-LLaMA_3.1-F55036?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_DB-FF6B6B?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

🚀 **[Live Demo](https://swetha-mindease.streamlit.app)**

</div>

---

## What It Does

1. User shares how they are feeling in a chat interface
2. **Crisis detection** checks for high-risk keywords — immediately shows emergency resources if detected
3. **RAG pipeline** retrieves the most relevant mental health content from a curated knowledge base
4. **Groq LLaMA 3.1** generates an empathetic, grounded response using the retrieved context
5. **Quick topic buttons** for Anxiety, Depression, Sleep, and Stress
6. All sessions are **anonymous** — no data stored, no accounts required

> **Problem:** Access to mental health support is limited by cost, availability, and stigma. MindEase provides a judgment-free, always-available space for emotional support — while always encouraging professional help and surfacing crisis resources when needed.

---

## Features

| Feature | Description |
|---------|-------------|
| RAG Pipeline | Retrieves relevant knowledge base content before generating responses |
| Crisis Detection | Keyword-based safety layer — bypasses LLM and shows 988, 741741, 911 |
| ChromaDB Vector Search | Semantic search finds relevant content even without exact keyword match |
| Groq LLM | LLaMA 3.1 generates warm, empathetic, non-diagnostic responses |
| Quick Topic Buttons | One-click access to Anxiety, Depression, Sleep, Stress support |
| Anonymous & Private | No user data stored, no accounts, ephemeral sessions |
| Live deployment | Deployed on Streamlit Cloud — accessible anywhere |

---

## How It Works

```
User sends message
        │
        ▼
Crisis Detection Layer
  Check for high-risk keywords
  (suicide, self-harm, want to die...)
        │
   ┌────┴────┐
   YES       NO
   │         │
   ▼         ▼
Show        ChromaDB Semantic Search
Emergency   Find top-3 relevant chunks
Resources   from knowledge base
988/741741       │
                 ▼
            Groq LLaMA 3.1
            question + context → response
                 │
                 ▼
            Empathetic response
            displayed in chat UI
```

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| RAG Framework | ChromaDB + Sentence Transformers |
| Embeddings | all-MiniLM-L6-v2 (384-dim vectors) |
| LLM | Groq API (LLaMA 3.1-8b-instant) |
| Vector Database | ChromaDB (persistent local storage) |
| Frontend | Streamlit |
| Deployment | Streamlit Cloud (Python 3.11) |

---

## Knowledge Base

MindEase's knowledge base covers 8 mental health topics:

- 😰 **Anxiety Management** — breathing techniques, grounding (5-4-3-2-1), journaling
- 😔 **Depression Support** — behavioral activation, social connection, routine
- 😤 **Stress Management** — time management, mindfulness, boundaries
- 😴 **Sleep Problems** — sleep hygiene, screen-free time, relaxation routines
- 💚 **Self-Care Practices** — physical, emotional, social, mental wellness
- 🆘 **Crisis Resources** — 988 Lifeline, Crisis Text Line, SAMHSA helpline
- 🧘 **Mindfulness & Meditation** — body scan, mindful breathing, walking meditation
- 💪 **Building Resilience** — growth mindset, social support, self-efficacy

---

## Installation

```bash
git clone https://github.com/ixsntg012-lab/MindEase.git
cd MindEase
pip install -r requirements.txt
```

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key
```

Get a free Groq API key: [console.groq.com](https://console.groq.com)

---

## Usage

```bash
streamlit run app.py
```

Open browser: `http://localhost:8501`

---

## Project Structure

```
MindEase/
│
├── data/
│   └── knowledge_base.txt      ← Curated mental health content
│
├── utils/
│   └── rag_pipeline.py         ← ChromaDB setup + retrieval + Groq generation
│
├── chroma_db/                  ← Vector database (auto-created, gitignored)
├── app.py                      ← Main Streamlit chat interface
├── requirements.txt
├── runtime.txt                 ← Python 3.11 pinned for Streamlit Cloud
└── README.md
```

---

## Responsible AI Design

MindEase was built with responsible AI principles:

- **Crisis detection first** — safety layer runs before any LLM call. High-risk messages always surface emergency resources, never generate AI responses
- **RAG grounding** — responses based on verified knowledge base, not LLM hallucination
- **No diagnosis** — system prompt explicitly prohibits diagnosing conditions or prescribing treatment
- **Always encourage professionals** — every response path includes encouragement to seek real help
- **Anonymous by design** — no user data collected, no session persistence
- **Clear disclaimer** — prominently displayed on every page

---

## Limitations & Future Work

**Phase 1 — Better Retrieval**
- Expand knowledge base with licensed mental health content
- Hybrid search — combine semantic + keyword retrieval
- Source citation — show which knowledge base section was used

**Phase 2 — Personalization**
- Mood tracking over session with trend visualization
- Coping strategy recommendations based on conversation history
- Multilingual support — Telugu, Hindi, Spanish

**Phase 3 — Safety Enhancements**
- Multi-level crisis detection (low/medium/high risk)
- Automatic escalation suggestions for persistent high-risk patterns
- Integration with therapist finder APIs

**Phase 4 — Production**
- User accounts with optional history (opt-in only)
- Voice input support via speech-to-text
- Mobile app via React Native

---

## ⚠️ Disclaimer

> MindEase is an **educational AI project** and is **not** a replacement for professional mental health care.
>
> If you are in crisis, please contact:
> - **988 Suicide & Crisis Lifeline** — call or text **988** (24/7)
> - **Crisis Text Line** — text **HOME** to **741741** (24/7)
> - **Emergency Services** — call **911**

---

## Author

**Swetha Kiran Veernapu**  
MS Computer Science @ UCF  
[LinkedIn](https://linkedin.com/in/swetha-kiran-veernapu) · [GitHub](https://github.com/ixsntg012-lab)

---

## License

MIT License

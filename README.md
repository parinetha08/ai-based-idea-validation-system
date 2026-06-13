# 🚀 AI-Powered Idea Validation System

An AI-powered platform that analyzes, validates, and scores startup or project ideas using multiple AI models (OpenAI, Gemini, and Ollama). It also supports multilingual input and provides structured feedback, market insights, and feasibility scoring.

Deploy link-
Frontend:https://ai-based-idea-validation-system-1.onrender.com
Backend:https://ai-based-idea-validation-system.onrender.com/docs

---

## 📌 Features

### 🤖 AI Capabilities
- Idea validation using LLMs (OpenAI / Gemini / Ollama)
- Smart scoring engine for idea quality
- Trend and market feasibility analysis
- Prompt engineering pipeline for structured evaluation

### 🌍 Multilingual Support
- Supports multiple Indian languages:
  - English 🇬🇧
  - Hindi 🇮🇳
  - Telugu 🇮🇳
- Built-in translation layer (`i18n` module)

### 🧠 BYOK (Bring Your Own Key)
- Users can provide their own API keys
- Supports:
  - OpenAI API
  - Gemini API
- Flexible model switching

### ⚡ Local AI Support
- Ollama integration for offline/local inference
- No API dependency required for local testing

### 🌐 Full Stack Architecture
- FastAPI backend
- Streamlit frontend
- Modular service-based design

---

## 🏗️ Project Structure

```

ai-based-idea-validation-system/
│
├── app/
│   ├── backend/        # FastAPI backend
│   ├── frontend/       # Streamlit UI
│   ├── core/           # Config & logging
│   ├── i18n/           # Language translation
│   ├── utils/          # Helper utilities
│   └── locales/        # Language JSON files
│
├── ai/                 # AI chains & prompts
├── docs/               # Documentation
├── tests/              # Test cases
├── .env.example        # Environment template
├── requirements.txt    # Dependencies
└── README.md

````

---

## ⚙️ Installation

### 1. Clone repository
```bash
git clone https://github.com/your-username/ai-based-idea-validation-system.git
cd ai-based-idea-validation-system
````

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key

MODEL_NAME=gpt-4.1-mini

APP_ENV=development
LOG_LEVEL=INFO

OLLAMA_BASE_URL=http://localhost:11434
```

---

## ▶️ Running the Project

### Start Backend (FastAPI)

```bash
uvicorn app.backend.main:app --reload
```

---

### Start Frontend (Streamlit)

```bash
streamlit run app/frontend/streamlit_app.py
```

---

## 🧪 Testing

Run tests using:

```bash
pytest
```

---

## 🔐 Security Notes

* Never commit `.env` file
* Use `.env.example` for sharing structure
* Rotate API keys if exposed accidentally

---

## 🧩 Tech Stack

* Python
* FastAPI
* Streamlit
* OpenAI API
* Google Gemini API
* Ollama (Local LLM)
* Pydantic
* Pytest

---

## 📈 Future Improvements

* Database integration (PostgreSQL / MongoDB)
* User authentication system
* Idea history tracking
* Deployment (Docker + Cloud)
* Advanced analytics dashboard

---

## 👨‍💻 Author

Built as an internship/hackathon project focused on AI-driven idea validation and multilingual support.

---

## 📜 License

This project is licensed under the MIT License.

```

---

If you want, I can next:
- :contentReference[oaicite:0]{index=0}
- or :contentReference[oaicite:1]{index=1}
- or :contentReference[oaicite:2]{index=2}
```

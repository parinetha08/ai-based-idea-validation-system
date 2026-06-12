# System Architecture - AI Idea Validator

## Overview
This system validates startup ideas using AI and returns structured insights like score, risks, and improvements.

---

## Architecture Flow

User Input (Idea)
        ↓
Frontend (Streamlit UI)
        ↓
API Layer (FastAPI - optional)
        ↓
AI Service Layer (LLM Prompt Engine)
        ↓
Scoring Engine (Rule + AI Hybrid)
        ↓
Structured JSON Output
        ↓
Results Dashboard

---

## Components

### 1. Frontend
- Streamlit dashboard
- Input form for startup ideas
- Result visualization (score cards, charts)

### 2. Backend
- FastAPI (optional)
- Handles request routing
- Connects frontend with AI engine

### 3. AI Layer
- Prompt-based evaluation system
- Generates:
  - Idea score
  - Market demand
  - Risks
  - Improvements

### 4. Scoring Engine
- Weighted scoring model:
  - Uniqueness (25%)
  - Feasibility (25%)
  - Market demand (30%)
  - Clarity (20%)

---

## Design Principle
- Keep AI structured output only (JSON)
- Avoid free-form responses
- Ensure reproducibility of results
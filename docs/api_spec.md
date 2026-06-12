# API Specification - AI Idea Validator

## Base URL
http://localhost:8000

---

## Endpoint: Validate Idea

### POST /validate

### Request Body:
{
  "idea": "AI app for farmers to detect crop diseases"
}

---

### Response:
{
  "idea_score": 82,
  "market_demand": "High",
  "risks": [
    "Data availability issues",
    "High competition in agri-tech"
  ],
  "improvements": [
    "Focus on one crop initially",
    "Add offline mode support"
  ],
  "similar_ideas": [
    "Plantix",
    "CropIn"
  ]
}

---

## Internal Flow

Request → Prompt Builder → LLM → Output Parser → JSON Response

---

## Error Handling

### 400:
- Empty idea input

### 500:
- AI service failure

---

## Notes
- All responses are structured JSON
- No raw text responses allowed
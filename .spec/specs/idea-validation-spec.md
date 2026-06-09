# Idea Validation Spec

## Input:
Startup idea text

## Output:
Structured JSON with:

{
  "idea_score": 0-100,
  "market_demand": "Low/Medium/High",
  "risks": [],
  "improvements": [],
  "similar_ideas": []
}

## Scoring Logic:
- Uniqueness: 25%
- Feasibility: 25%
- Market Demand: 30%
- Clarity: 20%

## Rules:
- Penalize vague ideas
- Reward specific use-cases
- Prefer real-world applicability

## AI Behavior:
- Act like a startup investor
- Be critical, not flattering
- Provide actionable feedback

## Example:
Input: "AI app for farmers"
Output:
- score: 78
- demand: High
- risks: competition, data availability
- improvements: add crop-specific focus
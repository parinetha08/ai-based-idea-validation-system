# Reproducibility Audit

## Goal:
Ensure consistent scoring for same idea input

## Method:
- Fixed prompt structure
- Deterministic scoring rules
- Temperature = 0 (for LLM)

## Checks:
- Same idea → same score
- No random variation in outputs

## Failure Cases:
- API variation
- prompt ambiguity
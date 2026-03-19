# Directive: Round 4 - Technical HR

## Objective
Assess deep technical knowledge and problem-solving through live HR evaluation guided by an AI rubric.

## Inputs
- Job description and skills
- Candidate resume/profile
- HR panel rating

## Execution Scripts Required
- `execution/generate_interview_rubric.py`: Generates the structured framework for the HR to follow.
- `execution/compute_stage_score.py`: Computes weighted final score.

## Expected Structured Output
```json
{
  "ai_score": 70,
  "human_score": 85,
  "final_score": 79.0,
  "status": "PASS",
  "feedback": "Deep knowledge on system design."
}
```

## Cutoff Logic
- Final score computed with weighting rule (e.g., AI 40% + Human 60%).
- Compared against `cutoff_round_4`.

## Edge Cases
- HR submits incomplete scores -> prompt for missing input.

## Retry Rules
- Same as round 1.

## State Transition Rules
- PASS -> Move to ROUND_5
- FAIL -> REJECTED

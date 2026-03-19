# Directive: Round 3 - Coding Interview

## Objective
Assess practical coding ability. This stage incorporates both AI evaluation and Human evaluation.

## Inputs
- Candidate's submitted code
- Problem statement
- Human Panel Score

## Execution Scripts Required
- `execution/analyze_code.py`: Evaluates code correctness and returns AI score.
- `execution/compute_stage_score.py`: Computes weighted final score.

## Expected Structured Output
```json
{
  "ai_score": 88,
  "human_score": 90,
  "final_score": 88.8,
  "status": "PASS",
  "feedback": "Clean architecture, minor syntax flaw."
}
```

## Cutoff Logic
- Final score computed with weighting rule (e.g., AI 60% + Human 40%).
- Compared against `cutoff_round_3`.

## Edge Cases
- Code doesn't compile -> AI score 0.

## Retry Rules
- Same as round 1.

## State Transition Rules
- PASS -> Move to ROUND_4
- FAIL -> REJECTED

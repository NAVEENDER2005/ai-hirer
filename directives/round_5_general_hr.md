# Directive: Round 5 - General HR

## Objective
Assess behavioral aspects and cultural fit.

## Inputs
- Candidate profile
- Behavioral questions rubric

## Execution Scripts Required
- `execution/generate_interview_rubric.py`: Provide behavioral guidance.
- `execution/compute_stage_score.py`: Computes weighted final score.

## Expected Structured Output
```json
{
  "ai_score": 50,
  "human_score": 90,
  "final_score": 78.0,
  "status": "PASS",
  "feedback": "Great cultural fit."
}
```

## Cutoff Logic
- Configured weighting (e.g. AI 30% + Human 70%).
- Compared against `cutoff_round_5`.

## Edge Cases
- Missing inputs return structured errors.

## Retry Rules
- Same as round 1.

## State Transition Rules
- PASS -> Move to HIRED (after final decision step confirms)
- FAIL -> REJECTED

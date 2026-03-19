# Directive: Round 2 - Aptitude Test

## Objective
Evaluate candidate logical reasoning and problem-solving through an aptitude test.

## Inputs
- Job details (title, required skills)
- Candidate ID

## Execution Scripts Required
- `execution/generate_aptitude_test.py`: Creates structured aptitude questions.
- `execution/evaluate_aptitude.py`: Evaluates and returns score.

## Expected Structured Output
```json
{
  "score": 75,
  "status": "PASS",
  "feedback": "Good logical deductive skills."
}
```

## Cutoff Logic
- Orchestrator handles `score >= cutoff_round_2`.

## Edge Cases
- Invalid answers structure -> Return structured error.

## Retry Rules
- Same as round 1.

## State Transition Rules
- PASS -> Move to ROUND_3
- FAIL -> REJECTED

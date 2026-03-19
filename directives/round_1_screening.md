# Directive: Round 1 - Screening Test

## Objective
Generate and evaluate an initial screening test for candidates based on the job requirements. This test filters out candidates completely unsuited for the role.

## Inputs
- Job details (title, description, required skills)
- Candidate details (if personalized)

## Execution Scripts Required
- `execution/generate_screening_test.py`: Creates a structured multiple-choice screening test in JSON format.
- `execution/evaluate_screening.py`: Evaluates the candidate's answers and computes a raw score between 0 and 100.

## Expected Structured Output
The evaluation script must output:
```json
{
  "score": 85,
  "status": "PASS",
  "feedback": "Strong understanding of basics."
}
```

## Cutoff Logic
- The orchestrator will pass the raw score from `evaluate_screening.py` and compare against `cutoff_round_1`.
- If `score >= cutoff_round_1`: PASS
- Otherwise: FAIL

## Edge Cases
- Candidate submits empty answers -> score 0
- Script fails to parse answers -> throw error, do not fail candidate silently.

## Retry Rules
- If orchestrator detects failure and `attempt_count < max_attempts`, candidate may retry.

## State Transition Rules
- PASS -> Move to ROUND_2
- FAIL (No retries left) -> REJECTED

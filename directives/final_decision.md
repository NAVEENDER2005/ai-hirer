# Directive: Final Decision

## Objective
Aggregate scores from all 5 rounds and compute a final, explainable recommendation.

## Inputs
- Array of stage results (Rounds 1-5).
- Job metadata and weightings for overall hiring.

## Execution Scripts Required
- `execution/compute_final_decision.py`

## Expected Structured Output
```json
{
  "final_score": 82.5,
  "hiring_confidence_index": 0.85,
  "recommendation": "HIRE",
  "reasoning": [
    "Consistent performance across coding and aptitude.",
    "Strong technical HR feedback.",
    "Average behavioral scores, but acceptable."
  ]
}
```

## Cutoff Logic
- Configured final threshold.
- If final score >= final_cutoff AND human confirms -> HIRED.

## Edge Cases
- Missing round data -> Return "INCOMPLETE".

## Retry Rules
- N/A

## State Transition Rules
- Orchestrator relies on human confirmation to change Application State to HIRED or REJECTED.

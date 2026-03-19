import json
import sys

def compute_decision(input_data: dict) -> dict:
    scores = input_data.get("stage_scores", [])
    
    if not scores:
        return {
            "final_score": 0,
            "hiring_confidence_index": 0.0,
            "recommendation": "INCOMPLETE",
            "reasoning": ["No stage scores provided."]
        }
    
    total = sum(scores)
    final_score = total / len(scores)
    
    confidence = final_score / 100.0
    
    cutoff = input_data.get("final_cutoff", 70.0)
    
    recommendation = "HIRE" if final_score >= cutoff else "REJECT"
    
    reasoning = [
        f"Average score across stages: {final_score:.2f}",
        f"Confidence index computed at {confidence:.2f}",
        "Strong overall performance." if recommendation == "HIRE" else "Fails to meet minimum threshold."
    ]
    
    return {
        "final_score": round(final_score, 2),
        "hiring_confidence_index": round(confidence, 2),
        "recommendation": recommendation,
        "reasoning": reasoning
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = json.loads(sys.argv[1])
        result = compute_decision(data)
        print(json.dumps(result))

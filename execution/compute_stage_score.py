import json
import sys

def compute(input_data: dict) -> dict:
    ai_score = input_data.get("ai_score", 0)
    human_score = input_data.get("human_score", 0)
    
    ai_weight = input_data.get("ai_weight", 0.5)
    human_weight = input_data.get("human_weight", 0.5)
    
    cutoff = input_data.get("cutoff", 0)
    
    final_score = (ai_score * ai_weight) + (human_score * human_weight)
    
    status = "PASS" if final_score >= cutoff else "FAIL"
    
    return {
        "final_score": round(final_score, 2),
        "status": status,
        "ai_score_used": ai_score,
        "human_score_used": human_score,
        "feedback": f"Computed Score: {final_score} against cutoff {cutoff}."
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = json.loads(sys.argv[1])
        result = compute(data)
        print(json.dumps(result))

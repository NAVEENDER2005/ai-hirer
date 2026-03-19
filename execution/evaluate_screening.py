import json
import sys

def evaluate(input_data: dict) -> dict:
    answers = input_data.get("answers", [])
    correct_count = 0
    total = len(answers)
    
    if total == 0:
        return {"score": 0, "status": "FAIL", "feedback": "No answers provided."}

    for answer in answers:
        if answer.get("selected") == "A":  # Dummy correct answer
            correct_count += 1
            
    score = (correct_count / total) * 100
    
    return {
        "score": score,
        "status": "PASS" if score > 0 else "FAIL", # Orchestrator does the cutoff checking, so status is just indicative here
        "feedback": f"Got {correct_count} out of {total} correct."
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = json.loads(sys.argv[1])
        result = evaluate(data)
        print(json.dumps(result))

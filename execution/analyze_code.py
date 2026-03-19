import json
import sys

def analyze(input_data: dict) -> dict:
    code = input_data.get("code", "")
    
    if not code.strip():
        return {
            "ai_score": 0,
            "feedback": "Empty code submission."
        }
        
    # Dummy static code analysis
    ai_score = 85
    if "syntax error" in code.lower():
        ai_score = 0
    elif "complexity" in code.lower():
        ai_score = 60
        
    return {
        "ai_score": ai_score,
        "feedback": "Code analysis completed. Architecture looks decent."
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = json.loads(sys.argv[1])
        result = analyze(data)
        print(json.dumps(result))

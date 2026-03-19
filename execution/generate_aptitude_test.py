import json
import uuid
import sys

def main(input_data: dict) -> dict:
    job_id = input_data.get("job_id")
    
    # Generic aptitude test structure
    questions = []
    for i in range(5):
        questions.append({
            "question_id": str(uuid.uuid4()),
            "type": "logic",
            "text": f"Logic question {i+1}?",
            "options": ["T", "F"],
            "correct_option": "T"
        })
        
    return {
        "test_id": str(uuid.uuid4()),
        "job_id": job_id,
        "questions": questions,
        "duration_minutes": 45
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = json.loads(sys.argv[1])
        result = main(data)
        print(json.dumps(result))

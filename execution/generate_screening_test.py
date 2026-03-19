import json
import uuid

def generate_screening_test(input_data: dict) -> dict:
    job_id = input_data.get("job_id")
    skills = input_data.get("required_skills", [])
    
    questions = []
    for skill in skills:
        # Dummy problem generation based on skill
        questions.append({
            "question_id": str(uuid.uuid4()),
            "skill": skill,
            "text": f"What is the primary use of {skill}?",
            "options": ["A", "B", "C", "D"],
            "correct_option": "A"
        })
        
    return {
        "test_id": str(uuid.uuid4()),
        "job_id": job_id,
        "questions": questions,
        "duration_minutes": 30
    }

if __name__ == "__main__":
    import sys
    data = json.loads(sys.argv[1])
    result = generate_screening_test(data)
    print(json.dumps(result))

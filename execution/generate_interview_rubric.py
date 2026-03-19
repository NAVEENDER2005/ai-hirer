import json
import uuid
import sys

def generate_rubric(input_data: dict) -> dict:
    stage_type = input_data.get("type", "technical") # technical or behavioral
    
    rubric = {
        "rubric_id": str(uuid.uuid4()),
        "stage": stage_type,
        "criteria": []
    }
    
    if stage_type == "technical":
        rubric["criteria"] = [
            {"id": "t1", "topic": "Architecture", "max_score": 10},
            {"id": "t2", "topic": "Problem Solving", "max_score": 10},
            {"id": "t3", "topic": "Coding Standards", "max_score": 10}
        ]
    else:
        rubric["criteria"] = [
            {"id": "b1", "topic": "Communication", "max_score": 10},
            {"id": "b2", "topic": "Teamwork", "max_score": 10},
            {"id": "b3", "topic": "Adaptability", "max_score": 10}
        ]
        
    return rubric

if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = json.loads(sys.argv[1])
        result = generate_rubric(data)
        print(json.dumps(result))

#chandrani editing this file
from fastapi import APIRouter, Request  # Added Request for handling JSON body in POST
import random

router = APIRouter(tags=["quiz"])

# I actually could have added this to a collection in mongodb
questions = [
    {
        "id": 1,
        "text": "What command lists directory contents?",
        "options": ["ls", "cd", "rm", "pwd"],
        "correct": "ls"
    },
    {
        "id": 2,
        "text": "Which command searches for text in files?",
        "options": ["find", "grep", "locate", "cat"],
        "correct": "grep"
    },
    {
        "id": 3,
        "text": "What changes file permissions?",
        "options": ["chmod", "chown", "mv", "cp"],
        "correct": "chmod"
    },
    {
        "id": 4,
        "text": "Which command displays the current directory?",
        "options": ["dir", "pwd", "path", "where"],
        "correct": "pwd"
    },
    {
        "id": 5,
        "text": "What removes a file?",
        "options": ["rm", "del", "erase", "unlink"],
        "correct": "rm"
    }
]

game_state = {"high_score": 0}
# god would hate me for not dockerizing this repo
@router.get("/question")
async def get_question():
    question = random.choice(questions)  # FIXED: return a random question instead of static
    return {
        "id": question["id"],
        "text": question["text"],
        "options": question["options"]
    }

# FIXED: changed GET to POST and added request parsing
@router.post("/answer")
async def submit_answer(request: Request):  # Use Request to parse incoming POST body
    data = await request.json()  # Properly extract JSON payload
    question_id = data.get("id")
    answer = data.get("answer")
    score = data.get("score", 0)

    if not question_id or not answer:  # FIXED: Added validation for missing question_id or answer
        return {"error": "Missing 'id' or 'answer' in the request"}  # Return error message for missing fields

    question = next((q for q in questions if q["id"] == question_id), None)
    if not question:
        return {"error": "Invalid question ID"}

    is_correct = answer == question["correct"]
    if is_correct:
        score += 10
        if score > game_state["high_score"]:
            game_state["high_score"] = score

    return {
        "is_correct": is_correct,
        "correct_answer": question["correct"],
        "score": score,
        "high_score": game_state["high_score"]
    }

@router.get("/highscore")
async def get_highscore():
    return {"high_score": game_state["high_score"]}

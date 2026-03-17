from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import json

from transcriber import transcribe_video
from interview import evaluate_interview_answers
from llm import llm
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RoleInput(BaseModel):
    role: str

@app.post("/generate-questions")
async def generate_questions(data: RoleInput):

    role = data.role

    prompt = f"""
Generate 5 technical interview questions for a {role}.

Return ONLY a JSON list.

Example:
[
 "Question 1",
 "Question 2",
 "Question 3",
 "Question 4",
 "Question 5"
]
"""

    response = llm.invoke(prompt)

    try:
        questions = json.loads(response.content)
    except:
        questions = [q.strip() for q in response.content.split("\n") if q]

    return {"questions": questions}


@app.post("/transcribe-chunk")
async def transcribe_chunk(video: UploadFile = File(...)):

    text = await transcribe_video(video)

    return {"text": text}

class AnswerItem(BaseModel):
    question: str
    answer: str

class InterviewInput(BaseModel):
    role: str
    answers: list[AnswerItem]

@app.post("/evaluate-interview")
async def evaluate_interview(data: InterviewInput):

    answers = data.answers

    results = await evaluate_interview_answers(answers)

    return {"evaluation": results}
from llm import llm
import json


def evaluate_answer(question, answer):

    prompt = f"""
You are an interview evaluator.

Question:
{question}

Candidate Answer:
{answer}

Return JSON:

{{
 "score": number,
 "feedback": "short explanation"
}}
"""

    response = llm.invoke(prompt)

    try:
        return json.loads(response.content)
    except:
        return {
            "score": 0,
            "feedback": response.content
        }
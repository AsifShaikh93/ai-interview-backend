from evaluator import evaluate_answer


async def evaluate_interview_answers(answers):

    results = []

    for qa in answers:

        evaluation = evaluate_answer(
            qa.question,
            qa.answer
        )

        results.append({
            "question": qa.question,
            "score": evaluation["score"],
            "feedback": evaluation["feedback"]
        })

    return results
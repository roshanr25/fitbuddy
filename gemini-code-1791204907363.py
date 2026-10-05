# gemini_service.py
def update_workout_plan(current_plan: str, feedback: str) -> str:
    prompt = f"""
    You are an expert personal trainer. Revise the following 7-day workout plan based on user feedback.

    [Original Plan]:
    {current_plan}

    [User Feedback]:
    {feedback}

    Provide the full updated 7-day schedule incorporating all requested changes.
    """
    return client.models.generate_content(model="gemini-1.5-pro", contents=prompt).text
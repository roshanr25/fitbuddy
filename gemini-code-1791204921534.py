# gemini_service.py
def generate_workout_plan(name: str, age: int, weight: int, goal: str, intensity: str) -> str:
    prompt = f"""
    Create a detailed, goal-oriented 7-day workout plan for:
    - Name: {name}, Age: {age}, Weight: {weight}kg
    - Fitness Goal: {goal}, Preferred Intensity: {intensity}

    Format in Markdown with Day 1 to Day 7 including warm-ups, exercises, sets/reps, and cooldowns.
    """
    return client.models.generate_content(model="gemini-1.5-pro", contents=prompt).text

def generate_nutrition_tip(goal: str) -> str:
    prompt = f"Provide 3 actionable, concise nutrition and recovery tips for target goal: '{goal}'."
    return client.models.generate_content(model="gemini-1.5-flash", contents=prompt).text
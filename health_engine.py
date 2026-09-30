def analyze_health(data):
    """Generate simple educational wellness insights from user-entered data."""

    insights = []
    actions = []

    sleep = float(data["sleep_hours"])
    steps = int(data["steps"])
    heart_rate = int(data["heart_rate"])
    water = float(data["water_liters"])
    goal = str(data.get("goal", "")).strip()

    # Sleep
    if sleep < 7:
        insights.append("The entered sleep duration is below 7 hours.")
        actions.append("Consider maintaining a consistent sleep schedule.")
    else:
        insights.append("The entered sleep duration is 7 hours or more.")

    # Activity
    if steps < 6000:
        insights.append("The entered activity level is below 6,000 steps.")
        actions.append("Consider adding a short walk or another comfortable activity.")
    else:
        insights.append("The entered activity level is at least 6,000 steps.")

    # Hydration
    if water < 2:
        insights.append("The entered water intake is below 2 liters.")
        actions.append("Review your hydration routine and drink water regularly.")
    else:
        insights.append("The entered water intake is at least 2 liters.")

    # Resting heart rate
    if heart_rate < 50 or heart_rate > 100:
        insights.append(
            "The entered resting heart-rate value is outside the simple demo "
            "range of 50–100 bpm."
        )
        actions.append(
            "If this value is unusual for you or you have symptoms, discuss it "
            "with a healthcare professional."
        )
    else:
        insights.append(
            "The entered resting heart-rate value is within the simple demo range."
        )

    if goal:
        actions.append(f"Keep daily actions aligned with your goal: {goal}.")

    return insights, actions

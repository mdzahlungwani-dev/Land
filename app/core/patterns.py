def detect_patterns(events):

    insights = []

    if len(events) > 10:
        insights.append("User is highly active.")

    return insights

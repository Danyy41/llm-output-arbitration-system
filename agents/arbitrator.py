def arbitrate(critiques):
    average_score = sum(c["score"] for c in critiques) / len(critiques)

    if average_score >= 8:
        verdict = "approved"
        action = "Answer can be used."
    elif average_score >= 5:
        verdict = "needs_revision"
        action = "Answer should be improved before use."
    else:
        verdict = "rejected"
        action = "Answer should not be used."

    return {
        "average_score": round(average_score, 2),
        "verdict": verdict,
        "action": action,
        "critiques": critiques
    }


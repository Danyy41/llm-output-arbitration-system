def arbitrate(critiques):
    average_score = sum(c["score"] for c in critiques) / len(critiques)

    if average_score >= 8:
        verdict = "approved"
    elif average_score >= 5:
        verdict = "needs_revision"
    else:
        verdict = "rejected"

    return {
        "average_score": average_score,
        "verdict": verdict,
        "critiques": critiques
    }

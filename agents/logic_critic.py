def check_logic(answer):
    """Simple logic critic that returns a fixed score and issue summary.

    Args:
        answer: The answer text to evaluate (unused in this simple implementation).

    Returns:
        dict: A dictionary with keys 'agent', 'score', and 'issue'.
    """
    return {
        "agent": "logic_critic",
        "score": 7,
        "issue": "Reasoning is mostly clear"
    }

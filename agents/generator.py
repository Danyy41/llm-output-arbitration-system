"""Simple answer generator used by tests.

Provides a generate_answer(question) function that returns a sample
string response. Keep this file minimal and side-effect free.
"""

def generate_answer(question: str) -> str:
    """Return a simple sample answer for the given question.

    Args:
        question: The input question string.

    Returns:
        A formatted sample answer string.
    """
    return f"This is a sample answer to: {question}"

    

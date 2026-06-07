import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def check_completeness(answer):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a completeness critic. Check if the answer fully addresses the user's question and whether anything important is missing. Return a short critique."
            },
            {
                "role": "user",
                "content": f"Evaluate this answer for completeness:\n\n{answer}"
            }
        ]
    )

    critique_text = response.choices[0].message.content

    return {
        "agent": "completeness_critic",
        "score": 6,
        "issue": critique_text
    }


    
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def check_logic(answer):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a logical consistency critic. Check if the reasoning is clear, consistent, and supported. Return a short critique."
            },
            {
                "role": "user",
                "content": f"Evaluate this answer for logical consistency:\n\n{answer}"
            }
        ]
    )

    critique_text = response.choices[0].message.content

    return {
        "agent": "logic_critic",
        "score": 7,
        "issue": critique_text
    }

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def check_facts(answer):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a factual accuracy critic. Check if the answer is factually correct. Return a short critique."
            },
            {
                "role": "user",
                "content": f"Evaluate this answer for factual accuracy:\n\n{answer}"
            }
        ]
    )

    critique_text = response.choices[0].message.content

    return {
        "agent": "factual_critic",
        "score": 8,
        "issue": critique_text
    }

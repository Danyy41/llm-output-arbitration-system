from pydantic import BaseModel


class Critique(BaseModel):
    agent: str
    score: int
    issue: str

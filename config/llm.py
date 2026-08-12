import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from utils.rate_limiter import rate_limiter


load_dotenv()


class RateLimitedLLM:
    def __init__(self):
        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0
        )

    def invoke(self, prompt):
        rate_limiter.wait()
        return self.llm.invoke(prompt)


llm = RateLimitedLLM()
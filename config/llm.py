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

    def with_structured_output(self, schema):
        rate_limited_llm = self

        class StructuredLLM:
            def invoke(self, prompt):
                rate_limiter.wait()
                structured_model = rate_limited_llm.llm.with_structured_output(schema)
                return structured_model.invoke(prompt)

        return StructuredLLM()


llm = RateLimitedLLM()
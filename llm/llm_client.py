from openai import OpenAI

from config import OPENROUTER_API_KEY
from config import MODEL_NAME
from config import TEMPERATURE

from llm.prompts import SYSTEM_PROMPT


class LLMClient:

    def __init__(self):

        self.client = OpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1"
        )

    def invoke(self, user_message: str):

        response = self.client.chat.completions.create(
            model=MODEL_NAME,
            temperature=TEMPERATURE,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        return response.choices[0].message.content


        
import os
import openai
from config.settings import OPENAI_SERVICE

class OpenAIService:
    def __init__(self):
        print("OPENAI key starts with:", os.getenv("OPENAI_API_KEY")[:5])
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_response(self, prompt,max_tokens = 100):
        response = self.client.chat.completions.create(
            model=OPENAI_SERVICE["model"],
            max_tokens=max_tokens,
            temperature=OPENAI_SERVICE["temperature"],
            top_p=OPENAI_SERVICE["top_p"],
            frequency_penalty=OPENAI_SERVICE["frequency_penalty"],
            presence_penalty=OPENAI_SERVICE["presence_penalty"],
            stop=OPENAI_SERVICE["stop"],
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
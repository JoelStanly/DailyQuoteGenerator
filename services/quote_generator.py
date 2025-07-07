from services.openai_service import OpenAIService
from config.settings import QUOTE_GENERATOR


class QuoteGenerator:
    def __init__(self, client: OpenAIService):
        self.client = client

    def generate_quote(self, prompt: str, max_tokens=QUOTE_GENERATOR["max_tokens"]):
        prompt = QUOTE_GENERATOR["base_prompt"].format(prompt=prompt)
        response = self.client.generate_response(prompt, max_tokens=max_tokens)
        return response
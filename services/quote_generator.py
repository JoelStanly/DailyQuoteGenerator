from services.openai_service import OpenAIService
from config.settings import QUOTE_GENERATOR


class QuoteGenerator:
    def __init__(self, client: OpenAIService):
        self.client = client

    def generate_quote(self, prompt: str, max_tokens=QUOTE_GENERATOR["max_tokens"]):
        prompt = (
            "Write a very short and original motivational quote based on the following theme:  "
            f"{prompt}. "
            "The quote should be uplifting, motivational, and suitable for daily inspiration. "
        )
        response = self.client.generate_response(prompt, max_tokens=max_tokens)
        return response
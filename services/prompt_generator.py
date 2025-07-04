from services.openai_service import OpenAIService
from config.settings import PROMPT_GENERATOR

class PromptGenerator:
    def __init__(self, client: OpenAIService):
        self.client = client

    def generate_prompt(self):
        prompt = (
            "Generate one creative, original prompt to be used for generating an inspirational quote. "
            "The prompt should describe a unique theme like courage, gratitude, resilience, etc."
            " It should be concise, engaging, and suitable for a daily motivational quote. "
        )
        return self.client.generate_response(prompt, max_tokens=PROMPT_GENERATOR["generate_prompt_max_tokens"])
    
    def extract_keywords(self, prompt_text: str):
        SKIP_KEYWORDS = {"quote", "theme", "image", "photo", "prompt", "inspired", "motivational", "inspiration", "inspire", "motivational", "inspirational", "daily", "quote", "quotes", "daily quote", "daily quotes"}
        prompt = (
            "Extract keywords from the following prompt for image searching: "
            f"{prompt_text}. "
            "Return them as a comma-separated list without quotes or extra text"
        )
        keywords = self.client.generate_response(prompt, max_tokens=PROMPT_GENERATOR["extract_keywords_max_tokens"])
        return [keyword.strip() for keyword in keywords.split(",") if keyword.strip() and keyword.strip().lower() not in SKIP_KEYWORDS]
from services.openai_service import OpenAIService
from config.settings import PROMPT_GENERATOR

class PromptGenerator:
    def __init__(self, client: OpenAIService):
        self.client = client

    def generate_prompt(self):
        prompt = PROMPT_GENERATOR["base_prompt"]
        return self.client.generate_response(prompt, max_tokens=PROMPT_GENERATOR["generate_prompt_max_tokens"])
    
    def extract_keywords(self, prompt_text: str):
        SKIP_KEYWORDS = PROMPT_GENERATOR["skip_keywords"]
        prompt = (
            "Extract keywords from the following prompt for image searching: "
            f"{prompt_text}. "
            "Return them as a comma-separated list without quotes or extra text"
        )
        keywords = self.client.generate_response(prompt, max_tokens=PROMPT_GENERATOR["extract_keywords_max_tokens"])
        return [keyword.strip() for keyword in keywords.split(",") if keyword.strip() and keyword.strip().lower() not in SKIP_KEYWORDS]
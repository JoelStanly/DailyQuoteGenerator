from services.image_generator import ImageGenerator
from services.openai_service import OpenAIService
from services.prompt_generator import PromptGenerator
from services.quote_generator import QuoteGenerator
from services.unsplash_service import UnsplashService

# local Testing
from dotenv import load_dotenv
load_dotenv()

def main():
    client = OpenAIService()
    prompt_generator = PromptGenerator(client)
    quote_generator = QuoteGenerator(client)
    unsplash_service = UnsplashService()
    image_generator = ImageGenerator()


    prompt = prompt_generator.generate_prompt()
    print(f"Generated Prompt: {prompt}")
    quote = quote_generator.generate_quote(prompt)
    print(f"Generated Quote: {quote}")
    keywords = prompt_generator.extract_keywords(prompt)
    print(f"Extracted Keywords: {keywords}")
    image_url, attribution = unsplash_service.fetch_random_image_url(keywords)
    print(f"Image URL: {image_url}")
    print(f"Attribution: {attribution}")
    image_generator.quote_image(image_url, quote, output_path="output/quoteImg.jpg")
    print("Image with Quote generated successfully.")



if __name__ == "__main__":
    main()
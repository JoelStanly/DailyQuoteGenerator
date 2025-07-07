PROMPT_GENERATOR = {
    "generate_prompt_max_tokens": 100,
    "extract_keywords_max_tokens": 20,
    "base_prompt": (
            "Generate one creative, original prompt to be used for generating an inspirational quote. "
            "The prompt should describe a unique theme like courage, gratitude, resilience, etc."
            " It should be concise, engaging, and suitable for a daily motivational quote. "
        ),
    "skip_keywords": {"quote", "theme", "image", "photo", "prompt", "inspired", "motivational", "inspiration", "inspire", "motivational", "inspirational", "daily", "quote", "quotes", "daily quote", "daily quotes"}
}
QUOTE_GENERATOR = {
    "max_tokens": 60,
    "base_prompt": (
        "Write a very short and original motivational quote based on the following theme:  "
        "{prompt}. "
        "The quote should be uplifting, motivational, and suitable for daily inspiration. "
    ),
}
OPENAI_SERVICE = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.9,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0.6,
    "stop": None,
}
UNSPLASH_SERVICE = {
    "orientation": "landscape",
    "count": 1,
}
IMAGE_SERVICE = {
    "font_path": "assets/contentfont/",
    "font_size": 40,
    "wrap_width": 40,
    "margin": 40,
    "header_path": "assets/headerfont/",
    "header_size": 48,
    "quote_header": "Daily Quote  {date}",
    "quote_date_format": "%B %d, %Y",
}
DISCORD_SERVICE = {
    "title": "Daily Quote",
    "attribution": "Image from Unsplash",
    "guild_name": "Daily Quote Guild",
    "channel_name": "daily-quotes",
}
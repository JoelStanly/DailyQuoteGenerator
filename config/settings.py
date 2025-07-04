PROMPT_GENERATOR = {
    "generate_prompt_max_tokens": 100,
    "extract_keywords_max_tokens": 20,
}
QUOTE_GENERATOR = {
    "max_tokens": 60,
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
    "font_path": "assets\\contentfont\\",
    "font_size": 40,
    "wrap_width": 40,
    "margin": 40,
    "header_path": "assets\\headerfont\\",
    "header_size": 48,
}
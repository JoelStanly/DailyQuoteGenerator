from datetime import datetime
from PIL import Image,ImageDraw, ImageFont
import requests
from io import BytesIO
import textwrap
import os
import random
from config.settings import IMAGE_SERVICE

class ImageGenerator:
    def __init__(self):
        pass

    def fetch_font(self, font_directory):
        font_files = [f for f in os.listdir(font_directory) if f.endswith('.ttf')]
        if not font_files:
            raise FileNotFoundError("No font files found in the specified directory.")
        else:
            random.shuffle(font_files)
        return os.path.join(font_directory, font_files[0])
    

    def quote_image(self,image_url,quote_text,output_path="output/quoteImg.jpg"):
        if image_url:
            try:
                response = requests.get(image_url)
                img = Image.open(BytesIO(response.content)).convert("RGBA")
            except Exception as e:
                print(f"Error fetching image from URL: {e}")
                img = Image.new("RGBA", (1080, 1080), (0, 0, 0, 255))  # Fallback image

        else:
            print("No image URL provided, using fallback image.")
            img = Image.new("RGBA", (1080, 1080), (0, 0, 0, 255))
        width, height = img.size

        overlay = Image.new("RGBA",img.size,(0,0,0,120))
        img = Image.alpha_composite(img,overlay)

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(self.fetch_font(IMAGE_SERVICE["font_path"]), IMAGE_SERVICE["font_size"])

        # Calculate text size and position
        wrapped_text = textwrap.fill(quote_text, width=IMAGE_SERVICE["wrap_width"])
        text_bbox = draw.textbbox((0,0),wrapped_text,font=font)
        text_height = text_bbox[3] - text_bbox[1]
        text_position = (IMAGE_SERVICE["margin"],height - text_height - 100)

        # Content
        draw.text(text_position,wrapped_text,font=font,fill="white")

        #Middle Top Header
        header_text = IMAGE_SERVICE["quote_header"].format(date=datetime.now().strftime(IMAGE_SERVICE["quote_date_format"]))
        header_font = ImageFont.truetype(self.fetch_font(IMAGE_SERVICE["header_path"]), IMAGE_SERVICE["header_size"])
        header_width = draw.textlength(header_text, font=header_font)
        header_position = ((width - header_width) // 2, IMAGE_SERVICE["margin"])
        #header
        draw.text(header_position, header_text, font=header_font, fill="white")

        os.makedirs(os.path.dirname(output_path),exist_ok=True)
        img.convert("RGB").save(output_path)
        print("Image Generated and saved")

        return output_path
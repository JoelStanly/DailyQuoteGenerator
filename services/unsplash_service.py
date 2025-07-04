import os
import random
import requests
from config.settings import UNSPLASH_SERVICE

class UnsplashService:
    def __init__(self):
        self.access_key = os.getenv("UNSPLASH_API_ACCESS_KEY")
        self.base_url = "https://api.unsplash.com/photos/random"
        self.auth_header = {"Authorization": f"Client-ID {self.access_key}"}

    def fetch_random_image_url(self, keywords):
        if not keywords:
            keywords = ["inspiration"]

        query = random.choice(keywords)
        params = {
            "query": query,
            "client_id": self.access_key,
            "count": UNSPLASH_SERVICE["count"],
            "orientation": UNSPLASH_SERVICE["orientation"]
        }
        headers = {
            "Accept-Version": "v1"
        }

        response = requests.get(self.base_url, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data:
                data = data[0]
            image_url = data.get("urls", {}).get("regular")
            attribution = data.get("user", {}).get("name", "Unsplash")

            download_link = data.get("links", {}).get("download")
            requests.get(download_link, headers=self.auth_header)

            return image_url, attribution
        else:
            print(f"Error fetching image: {response.status_code} - {response.text}")
            return None, None

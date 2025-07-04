import os
import requests

class LinkedInService:
    def __init__(self):
        self.access_token = os.getenv("LINKEDIN_ACCESS_TOKEN")
        self.api_url = "https://api.linkedin.com/v2"

    def post_quote_image(self, image_path, attribution):
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0"
        }
        message = (
            "🌟 Here's your daily inspiration! #Motivation #QuoteOfTheDay\n\n"
            f"📸 Picture from Unsplash by {attribution}"
        )

        payload = {
            "author": f"urn:li:person:{os.getenv('LINKEDIN_PERSON_URN')}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": message
                    },
                    "shareMediaCategory": "IMAGE",
                    "media": [
                        {
                            "status": "READY",
                            "description": {
                                "text": attribution
                            },
                            "media": image_path,
                            "title": {
                                "text": "DailyQuote"
                            }
                        }
                    ]
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }
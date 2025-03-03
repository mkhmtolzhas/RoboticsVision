from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    def __init__(self, api_key: str = os.getenv("INFOBIP_API_KEY"), api_url: str = os.getenv("INFOBIP_API_URL")):
        self.api_key = api_key
        self.api_url = api_url


settings = Settings()

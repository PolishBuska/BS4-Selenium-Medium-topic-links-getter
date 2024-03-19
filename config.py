
import os
from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()

        self.base_url = os.getenv("BASE_URL")
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")


def get_config():
    return Config()

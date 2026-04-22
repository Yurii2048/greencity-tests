import os
from pathlib import Path

from dotenv import load_dotenv

dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

class Config:
    LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
    LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")
    NEW_USER_PASSWORD = os.getenv("NEW_USER_PASSWORD")
    NEW_USER_USERNAME = os.getenv("NEW_USER_USERNAME")

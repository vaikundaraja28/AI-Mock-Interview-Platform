from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent

DATABASE_PATH = BASE_DIR / "database" / "interview.db"

APP_NAME = "AI Mock Interview Platform"

APP_VERSION = "1.0.0"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
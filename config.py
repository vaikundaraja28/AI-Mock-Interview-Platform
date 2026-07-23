from pathlib import Path
from pathlib import Path

import os

from dotenv import load_dotenv


load_dotenv()


BASE_DIR = Path(__file__).parent


DATABASE_PATH = (
    BASE_DIR
    / "database"
    / "interview.db"
)


GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY",
    ""
)
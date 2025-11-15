from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
API_BASE = os.getenv("OPENAI_API_BASE") or None
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE_BYTES", 10 * 1024 * 1024))  # 10 МБ
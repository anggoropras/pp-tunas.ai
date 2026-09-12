import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "TUNAS AI")
APP_ENV = os.getenv("APP_ENV", "development")
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "google")
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-2.5-flash")
VECTOR_DB = os.getenv("VECTOR_DB", "chroma")
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "./vector_db")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1000"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "200"))
TOP_K = int(os.getenv("TOP_K", "5"))

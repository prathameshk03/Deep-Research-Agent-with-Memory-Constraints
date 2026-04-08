import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Constraints
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 2000))
MAX_CHUNKS_PER_QUERY = int(os.getenv("MAX_CHUNKS_PER_QUERY", 3))
MAX_TOTAL_CHUNKS = int(os.getenv("MAX_TOTAL_CHUNKS", 8))
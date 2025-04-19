import os
from dotenv import load_dotenv

load_dotenv()

KEYWORD = os.getenv("KEYWORD")
LOCATION = os.getenv("LOCATION")

print(f"Searching jobs for: {KEYWORD} in {LOCATION}")

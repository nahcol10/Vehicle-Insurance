import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB Configuration
MONGODB_URL = os.getenv("MONGODB_URLX")

# AWS Configuration
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

# App Configuration
APP_HOST = os.getenv("APP_HOST", "0.0.0.0")  # Default if not found
APP_PORT = int(os.getenv("APP_PORT", 5000))  # Convert to integer with default

"""
Configuration settings for Banking Bot
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Mistral AI Configuration
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "")
MISTRAL_MODEL = "mistral-large-latest"
MISTRAL_MAX_TOKENS = 1000
MISTRAL_TEMPERATURE = 0.7

# Streamlit Configuration
APP_TITLE = "🏦 Banking Bot Assistant"
APP_PAGE_TITLE = "Banking Bot"
APP_ICON = "🏦"
APP_LAYOUT = "wide"

# Chat Configuration
DEFAULT_MESSAGE = "Ask me about banking services..."
CHAT_INPUT_PLACEHOLDER = "Ask me about banking services..."

# System Prompt
BANKING_SYSTEM_PROMPT = """You are an expert banking assistant chatbot. You help customers with:
- Account information and balances
- Transaction history
- Money transfers
- Loan information
- Credit card services
- Investment advice
- Banking fees and charges
- Customer service issues

Be professional, helpful, and provide clear explanations. Always prioritize customer security and privacy.
If you don't have specific information, ask clarifying questions or recommend contacting the bank directly for sensitive matters."""

def validate_config():
    """Validate that all required configuration is present"""
    if not MISTRAL_API_KEY:
        raise ValueError("MISTRAL_API_KEY environment variable is not set. Please add it to your .env file.")
    return True

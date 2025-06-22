from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from environment
openai_api_key = os.getenv("OPENAI_API_KEY")

# Ensure the key is available
if not openai_api_key:
    raise ValueError("❌ OPENAI_API_KEY not found in .env file")

# Create ChatOpenAI model instance
model = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=1.0,  # More stable output
    max_tokens=50,    # More reasonable token count
    openai_api_key=openai_api_key
)

# Query the model
result = model.invoke("Write a 5-line poem on cricket")

# Print result
print(result.content)

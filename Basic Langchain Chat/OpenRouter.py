import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Load .env variables
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# OpenRouter base URL (OpenAI-compatible)
openrouter_url = "https://openrouter.ai/api/v1"

# List of available models with labels
available_models = {
    "1": ("OpenAI GPT-3.5 Turbo", "openai/gpt-3.5-turbo"),
    "2": ("OpenAI GPT-4 Turbo", "openai/gpt-4-turbo"),
    "3": ("Claude 3 Sonnet", "anthropic/claude-3-sonnet"),
    "4": ("Claude 3 Opus", "anthropic/claude-3-opus"),
    "5": ("Mistral 7B Instruct", "mistralai/mistral-7b-instruct"),
    "6": ("Gemini Pro", "google/gemini-pro"),
    "7": ("LLaMA 3 70B", "meta-llama/llama-3-70b-instruct"),
    "8": ("Command R+", "cohere/command-r-plus")
}

# Print model selection menu
print(" Choose an LLM to query via OpenRouter:\n")
for key, (name, _) in available_models.items():
    print(f"{key}. {name}")

# Take user input
choice = input("\nEnter the number of the model you want to use: ").strip()

# Validate input
if choice not in available_models:
    print(" Invalid choice. Exiting.")
    exit(1)

model_name = available_models[choice][1]
print(f"\n You selected: {available_models[choice][0]} ({model_name})")

# Initialize LangChain LLM
llm = ChatOpenAI(
    openai_api_key=api_key,
    openai_api_base=openrouter_url,
    model=model_name
)

# User prompt
query = input("\n Enter your prompt: ")

# Call LLM
response = llm([HumanMessage(content=query)])
print("\n Response:\n", response.content)

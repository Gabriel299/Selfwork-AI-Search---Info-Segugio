import os
from dotenv import load_dotenv

load_dotenv('.env')

### LLM in Locale
# class Config:
#   LLM_MODEL = "llama3.2"
#   LLM_MODEL_LOW = "llama3.2"
#   AI_API_URL = "http://localhost:11434/v1"
#   AI_API_KEY = "ollama"

### LLM su OpenAI
class Config:
  LLM_MODEL = "gpt-4o"
  LLM_MODEL_LOW = "gpt-4o-mini"
  AI_API_URL = "https://api.openai.com/v1"
  AI_API_KEY = os.environ['OPENAI_API_KEY']

  # TAVILY
  TAVILY_API_KEY = os.environ['TAVILY_API_KEY']
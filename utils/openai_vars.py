import os
import openai
from dotenv import load_dotenv

load_dotenv()

# openai.api_key = os.environ['OPENAI_API_KEY']
llm_name = "gpt-3.5-turbo"

def load_openai_key():
    openai.api_key = os.environ['OPENAI_API_KEY']
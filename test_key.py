from dotenv import load_dotenv
import os

env_path = os.path.join(os.getcwd(), ".env")
load_dotenv(dotenv_path=env_path, override=True)

print("ENV FILE PATH:", env_path)

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("❌ GROQ_API_KEY NOT LOADED")
else:
    print("✅ GROQ_API_KEY LOADED:", api_key[:6] + "********")
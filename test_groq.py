from dotenv import load_dotenv
load_dotenv()

import os
from groq import Groq

print("KEY:", os.getenv("GROQ_API_KEY")[:8])

client = Groq()

response = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[{"role": "user", "content": "Say hello"}],
)

print(response.choices[0].message.content)
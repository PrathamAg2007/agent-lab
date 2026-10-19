import os
from dotenv import load_dotenv
from google import genai
import time

load_dotenv()

prompt = "Write a one line slogan for a coffee shop."

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

for temp in [0.0, 0.0, 0.4, 0.8, 1.5, 1.5]:
    response = client.models.generate_content(
        model = "gemini-3.5-flash-lite",
        contents = prompt,
        config = genai.types.GenerateContentConfig(temperature = temp)
    )
    print(temp, '----', response.text)
    time.sleep(2)



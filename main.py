import os
from pickle import TRUE
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()


client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

# for temp in [0.0, 0.0, 0.4, 0.8, 1.5, 1.5]:
#     response = client.models.generate_content(
#         model = "gemini-3.5-flash-lite",
#         contents = prompt,
#         config = genai.types.GenerateContentConfig(temperature = temp)
#     )
#     print(temp, '----', response.text)
#     time.sleep(2)

prompt = "Hello there, what is your name?"

stream = client.interactions.create(
    model = "gemini-3.5-flash-lite",
    system_instruction = "You are a strict interviewer",
    input = prompt,
    generation_config = {
        "thinking_level" : "low",
        "max_output_tokens" : 200
    },
    stream = True
)
for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="")

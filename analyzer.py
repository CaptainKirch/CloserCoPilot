import openai
import os
from dotenv import load_dotenv
from prompts.base_prompt import BASE_PROMPT

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = "YOUR_API_KEY_HERE"

def analyze_transcript(transcript_text):
    # Combine prompt + transcript
    full_prompt = BASE_PROMPT + "\n\nTranscript:\n" + transcript_text

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a senior sales coach analyzing recorded calls."},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.7,
        max_tokens=1000
    )

    return response["choices"][0]["message"]["content"]

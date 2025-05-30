import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

def gpt_generate_query(prompt):
    messages = [
        {"role": "system", "content": "You are a helpful assistant that turns questions into concise Google search queries."},
        {"role": "user", "content": prompt}
    ]
    resp = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=32)
    return resp['choices'][0]['message']['content'].strip()

def gpt_summarize(text):
    if not text:
        return "No article text available."
    prompt = f"Summarize the following article in a few sentences:\n\n{text[:3500]}"
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=160
    )
    return resp['choices'][0]['message']['content'].strip()

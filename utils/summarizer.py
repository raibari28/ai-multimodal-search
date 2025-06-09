import openai
import os

# Validate that the OpenAI API key is available before creating the client.
_openai_key = os.environ.get("OPENAI_API_KEY")
if not _openai_key:
    raise RuntimeError(
        "OPENAI_API_KEY environment variable must be set to use the summarizer"
    )

client = openai.OpenAI(api_key=_openai_key)

def gpt_generate_query(prompt):
    messages = [
        {"role": "system", "content": "You are a helpful assistant that turns content or questions into concise Google search queries."},
        {"role": "user", "content": prompt}
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=48
    )
    return response.choices[0].message.content.strip()

def gpt_summarize(text):
    if not text:
        return "No article text available."
    prompt = f"Summarize and analyze the following (document and web source):\n\n{text[:3500]}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=256
    )
    return response.choices[0].message.content.strip()

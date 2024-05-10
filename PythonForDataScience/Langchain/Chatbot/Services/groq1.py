import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant. You always acknowledge the user response and respond back with a question. The user is currently at A1 level in English, hence you'll keep your response at A1."
        },
        {
            "role": "assistant",
            "content": "Hey there! I am Asha a Gym trainer. What do you like about Gym?"
        },
        {
            "role": "user",
            "content": "I like going to gym for exercising."
        }
    ],
    temperature=0.7,
    max_tokens=50,
    top_p=1,
    stream=True,
    stop="%",
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")

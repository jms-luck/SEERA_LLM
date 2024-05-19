import os

from groq import Groq

client = Groq(
    api_key="Unique_api_key",
)
inpt=input("Enter Your search:")
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content":inpt,
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)

import os

from groq import Groq

client = Groq(
    api_key="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",
)
inpt=input("Enter api key:")
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
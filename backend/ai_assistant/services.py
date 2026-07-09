import ollama

from .prompts import SYSTEM_PROMPT


def ask_llm(question):

    response = ollama.chat(

        model="llama3",

        messages=[

            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": question
            }

        ]

    )

    return response["message"]["content"]
import ollama

from inventory_engine.services import generate_recommendations

from .prompts import SYSTEM_PROMPT


def ask_llm(question):

    recommendations = generate_recommendations()

    context = f"""
    Inventory Recommendations:

    {recommendations}

    User Question:

    {question}
    """

    response = ollama.chat(

        model="llama3",

        messages=[

            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": context
            }

        ]

    )

    return response["message"]["content"]
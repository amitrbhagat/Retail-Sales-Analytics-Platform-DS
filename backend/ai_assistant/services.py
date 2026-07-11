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


def get_inventory():

    return generate_recommendations()


def get_forecast():

    return {
        "message": "Forecast API is ready. Connect best_model.pkl here."
    }


def get_analytics():

    return {
        "message": "Analytics API is ready. Connect analytics queries here."
    }
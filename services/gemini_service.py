from groq import Groq

from config import GROQ_API_KEY


client = Groq(
    api_key=GROQ_API_KEY
)


def ask_gemini(prompt):

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"ERROR: {e}"
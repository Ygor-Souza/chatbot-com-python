from google import genai
from google.genai import types

client = genai.Client(api_key="")

print("Chat começa aqui... Digite 'endchat' para encerrar")

user_input = input("User: ")

while user_input.lower() != "endchat":
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=user_input,
        config=types.GenerateContentConfig(
            system_instruction="Responda em uma linha, com no máximo 50 caracteres"
        )
    )

    print("Statbot:", response.text)
    user_input = input("User: ")

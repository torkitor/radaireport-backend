import os, json
import openai

# Carga tu API key de OpenAI desde entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

# Función manejadora de Vercel
def handler(request):
    data = request.get_json() or {}
    user_message = data.get("message", "")

    # Lee tu prompt maestro
    with open("prompt_maestro.txt", encoding="utf-8") as f:
        system_prompt = f.read()

    # Llamada a la IA
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_message}
        ]
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"reply": resp.choices[0].message.content})
    }

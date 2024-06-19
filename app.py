from flask import Flask, request, jsonify
from openai import OpenAI 
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask(__name__)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

model_natural_lang = 'gpt-4o'
model_audio_to_text = 'whisper-1'

@app.route('/', methods=['GET'])
def home():
    return "oi"


# @app.route('/', methods=['GET'])
# def generate_content():
#     # data = request.get_json()
#     # client_profile = data.get('clientProfile')
#     # past_success_content = data.get('pastSuccessContent')
#     # theme = data.get('theme')

#     # prompt = f"Baseado no perfil do cliente: {client_profile}, conteúdos de sucesso anteriores: {past_success_content}, crie um post para LinkedIn sobre o tema: {theme}."

#     # response = openai.Completion.create(
#     #     engine="text-davinci-003",
#     #     prompt=prompt,
#     #     max_tokens=500
#     # )

#     # generated_content = response.choices[0].text.strip()

#     return "oi"

completion = client.chat.completions.create(
  model=model_natural_lang,
  messages=[
    {"role": "system", "content": "You are a helpful assistant. Help me with my math homework!"}, # <-- This is the system message that provides context to the model
    {"role": "user", "content": "Hello! Could you solve 2+2?"}  # <-- This is the user message for which the model will generate a response
  ]
)

print("Assistant: " + completion.choices[0].message.content)

if __name__ == '__main__':
    app.run(debug=True)

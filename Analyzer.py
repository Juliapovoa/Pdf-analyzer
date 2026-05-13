 from openai import OpenAI
from PyPDF2 import PdfReader
from google.colab import files
from dotenv import load_dotenv
import json
import os

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

uploaded = files.upload()
nome_arquivo = list(uploaded.keys())[0]

reader = PdfReader(nome_arquivo)
texto_pdf = "".join(page.extract_text() for page in reader.pages)

pergunta = input("Digite sua pergunta: ")

prompt = f"""
Você é um analista de documentos.

Documento:
{texto_pdf}

Pergunta:
{pergunta}

Responda SOMENTE em JSON válido, sem nenhum texto fora dele, sem marcadores de código:

{{
  "type": "text",
  "text": "resposta em markdown com títulos, listas e destaques",
  "source": "{nome_arquivo}",
  "suggestions": [
    "<pergunta de acompanhamento relevante sobre o documento>",
    "<pergunta de acompanhamento relevante sobre o documento>",
    "<pergunta de acompanhamento relevante sobre o documento>"
  ]
}}
"""

resposta = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.3
)

conteudo = resposta.choices[0].message.content.strip()

if "```" in conteudo:
    conteudo = conteudo.split("```")[1]
    if conteudo.startswith("json"):
        conteudo = conteudo[4:].strip()

try:
    data = json.loads(conteudo)
    print(json.dumps(data, ensure_ascii=False, indent=2))
except json.JSONDecodeError:
    print("Não foi possível parsear o JSON. Resposta bruta:")
    print(conteudo)

tokens_entrada = resposta.usage.prompt_tokens
tokens_saida = resposta.usage.completion_tokens
custo = (tokens_entrada * 0.00000040) + (tokens_saida * 0.00000160)

print(f"\nTokens usados: {tokens_entrada} entrada / {tokens_saida} saída")
print(f"Custo estimado: US$ {custo:.6f}")

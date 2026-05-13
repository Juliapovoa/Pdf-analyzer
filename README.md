# Analisador de Documentos com IA

Script que recebe um arquivo PDF e uma pergunta em linguagem natural,
e retorna uma resposta estruturada em JSON usando a API da OpenAI.

## Requisitos

- Python 3.8+
- Conta na OpenAI com chave de API

## Instalação
```bash
pip install openai PyPDF2 python-dotenv
```
## Configuração

No Google Colab, rode isso numa célula antes do script principal:

```python
with open(".env", "w") as f:
    f.write("OPENAI_API_KEY=sua_chave_aqui")
```

## Como executar

O script foi desenvolvido para rodar no Google Colab.
Crie o `.env` com sua chave conforme a seção acima
Abra o arquivo `analyzer.py` no Colab e execute célula por célula.
Ao rodar, ele vai pedir para fazer upload do PDF e digitar a pergunta.

## Exemplo de saída

{
  "type": "text",
  "text": "### Cursos Complementares\n\n- Curso de Aleitamento Materno (60h) - UFRN",
  "source": "curriculo.pdf",
  "suggestions": [
    "Quais habilidades estão listadas no currículo?",
    "Qual é o objetivo profissional do candidato?",
    "Quais são as experiências profissionais listadas?"
  ]
}

## Modelo utilizado

Foi utilizado o modelo `gpt-4.1-mini` da OpenAI.

**Justificativa:** o modelo equilibra bem custo e desempenho para tarefas de
análise de texto. Ele suporta contextos longos, o que é essencial para processar
documentos PDF completos, e tem boa capacidade de seguir instruções de formato
JSON, garantindo respostas estruturadas e parseáveis.

## Estimativa de custo

Ao final de cada execução, o script exibe automaticamente:
- Quantidade de tokens usados na entrada e na saída
- Custo estimado em dólares com base no preço do modelo

Preços utilizados (gpt-4.1-mini):
- Entrada: US$ 0.40 por 1M de tokens
- Saída: US$ 1.60 por 1M de tokens

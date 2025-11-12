# contato_com_llm.py

from openai import OpenAI
import json
import re

client_openai = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="local"  # qualquer valor serve quando rodando localmente
)

def recebe_linha_e_retorna_json(linha):
    resposta_do_llm = client_openai.chat.completions.create(
        model="google/gemma-3-1b",
        messages=[
            {"role": "system", "content": """
            Você é um especialista em análise de dado e conversão de dados para json.
            Você receberá uma linha de texto que é uma resenha de um aplicativo em um marketplace online.
            Eu quero que você analise essa resenha, e me retorne um jason com as seguintes chaves:
            - 'usuario': O nome do usuario que fez a resenha.
            - 'resenha_original': A resenha original completa.
            - 'resenha_pt': A resenha traduzida para o português.
            - 'avaliação': Uma avaliação se essa resenha é positiva, negativa ou neutra.
            """},
            {"role": "user", "content": f"Resenha: {linha}"}
        ],
        temperature=0.0)
    
    resposta = resposta_do_llm.choices[0].message.content.replace("```json", "").replace("```", "")
    # resposta = re.sub(r"```[\s\S]*?```", "", resposta).strip()
    print(resposta)
    return resposta

    #     # Pega o texto da resposta (compatível com LM Studio, LocalAI, etc.)

    # resposta = resposta_do_llm.choices[0].message.content


    # # Limpa blocos markdown e espaços extras
    # resposta = re.sub(r"```[\s\S]*?```", "", resposta).strip()
    # resposta = resposta.replace("```json", "").replace("```", "").strip()

    # print("🟩 Resposta limpa:\n", resposta)

    # # Tenta converter o JSON diretamente
    # try:
    #     return json.loads(resposta)
    # except json.JSONDecodeError:
    #     print("⚠️ Erro ao decodificar JSON. Retornando texto original.")
    #     return {"erro": "Formato inválido", "conteudo": resposta}
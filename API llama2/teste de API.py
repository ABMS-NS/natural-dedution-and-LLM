import requests

# Substitua pelo seu token Hugging Face
HUGGING_FACE_API_KEY = "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"

# URL da API do Llama 2 no Hugging Face (verifique o nome exato do modelo no Hugging Face)
api_url = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b-chat-hf"

headers = {
    "Authorization": f"Bearer {HUGGING_FACE_API_KEY}"
}

def perguntar_llama2(pergunta):
    payload = {
        "inputs": pergunta,
        "parameters": {
            "temperature": 0.5,
            "max_new_tokens": 50
        }
    }
    
    response = requests.post(api_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        resposta = response.json()
        return resposta[0]['generated_text']
    else:
        print(f"Erro {response.status_code}: {response.text}")
        return None

# Exemplo de uso
pergunta = "Qual é a capital da França?"
resposta = perguntar_llama2(pergunta)
print("Resposta:", resposta)

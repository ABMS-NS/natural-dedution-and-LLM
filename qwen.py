from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

# Substitua pelo seu token de acesso da Hugging Face
HUGGING_FACE_API_TOKEN = "SEUTOKENAQUI"

# Inicializa o app FastAPI
app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

class PromptResponse(BaseModel):
    answer: str

@app.post("/generate", response_model=PromptResponse)
async def generate_answer(request: PromptRequest):
    try:
        headers = {
            "Authorization": f"Bearer {HUGGING_FACE_API_TOKEN}"
        }
        # Substitua 'modelo' pelo nome do modelo que você deseja usar
        response = requests.post(
            "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-72B-Instruct",
            headers=headers,
            json={"inputs": request.prompt}
        )
        response.raise_for_status()
        data = response.json()
        # Extrair a resposta do modelo
        answer = data[0]['generated_text']
        return PromptResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar: {e}")

@app.get("/")
async def root():
    return {"message": "API para interação com Hugging Face"}

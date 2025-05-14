from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ConteudoInput(BaseModel):
    conteudo_gerado: str

@app.post("/diagnostico")
def diagnostico(req: ConteudoInput):
    return {
        "resultado": f"Diagnóstico gerado com base neste conteúdo: {req.conteudo_gerado}"
    }

@app.post("/reflexion")
def reflexion(req: ConteudoInput):
    return {
        "resposta": f"Aqui está uma reflexão sobre o conteúdo recebido: {req.conteudo_gerado}"
    }

@app.post("/quiz")
def quiz(req: ConteudoInput):
    return {
        "pergunta": f"Com base no tema enviado, aqui vai uma pergunta: Qual é o ponto principal de '{req.conteudo_gerado}'?",
        "alternativas": ["A) Exemplo 1", "B) Exemplo 2", "C) Exemplo 3", "D) Exemplo 4"],
        "correta": "A"
    }

@app.post("/avaliacao")
def avaliacao(req: ConteudoInput):
    return {
        "nota": 8.5,
        "comentario": f"Avaliação automática do conteúdo recebido: {req.conteudo_gerado}"
    }

@app.post("/summary")
def summary(req: ConteudoInput):
    return {
        "resumo": f"Resumo automático do conteúdo: {req.conteudo_gerado[:100]}..."
    }

@app.post("/feedback")
def feedback(req: ConteudoInput):
    return {
        "feedback": f"Feedback gerado com base no conteúdo: {req.conteudo_gerado}"
    }

@app.post("/memoria")
def memoria(req: ConteudoInput):
    return {
        "registro": f"O seguinte conteúdo foi processado e armazenado: {req.conteudo_gerado}"
    }

@app.post("/observer")
def observer(req: ConteudoInput):
    return {
        "observacao": f"A observação foi feita sobre o seguinte conteúdo: {req.conteudo_gerado}"
    }

@app.post("/metaphors")
def metaphors(req: ConteudoInput):
    return {
        "metafora": f"Isto pode ser comparado a um rio fluindo: {req.conteudo_gerado}"
    }

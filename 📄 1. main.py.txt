from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ConteudoInput(BaseModel):
    conteudo_gerado: str

@app.post("/diagnostico")
def diagnostico(req: ConteudoInput):
    return {
        "resultado": f"Diagnóstico baseado em: {req.conteudo_gerado}"
    }

@app.post("/reflexion")
def reflexion(req: ConteudoInput):
    return {
        "resposta": f"Reflexão sobre o conteúdo: {req.conteudo_gerado}"
    }

@app.post("/quiz")
def quiz(req: ConteudoInput):
    return {
        "pergunta": "Qual é a função da acentuação gráfica?",
        "alternativas": ["A) Embelezar o texto", "B) Indicar entonação", "C) Marcar sílaba tônica", "D) Nada"],
        "correta": "C"
    }

@app.post("/avaliacao")
def avaliacao(req: ConteudoInput):
    return {
        "nota": 9.0,
        "comentario": "Conteúdo muito bem estruturado!"
    }

@app.post("/summary")
def summary(req: ConteudoInput):
    return {
        "resumo": f"Resumo: {req.conteudo_gerado[:100]}..."
    }

@app.post("/feedback")
def feedback(req: ConteudoInput):
    return {
        "feedback": "Você está evoluindo bem! Continue assim."
    }

@app.post("/memoria")
def memoria(req: ConteudoInput):
    return {
        "registro": f"Conteúdo salvo: {req.conteudo_gerado}"
    }

@app.post("/observer")
def observer(req: ConteudoInput):
    return {
        "observacao": f"Analisando: {req.conteudo_gerado}"
    }

@app.post("/metaphors")
def metaphors(req: ConteudoInput):
    return {
        "metafora": f"Isso é como plantar sementes no jardim do conhecimento: {req.conteudo_gerado}"
    }

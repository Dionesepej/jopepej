from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import yaml
from typing import List

app = FastAPI()

class RegistroHistorico(BaseModel):
    nome_agente: str
    descricao: str
    acoes: List[str]

@app.post("/registrarHistoricoOmega")
def registrar_historico(req: RegistroHistorico):
    caminho = "registro_de_agentes.yaml"
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            dados = yaml.safe_load(f) or {}
    except FileNotFoundError:
        dados = {"agentes": []}

    atualizado = False
    for ag in dados["agentes"]:
        if ag["nome_agente"].lower() == req.nome_agente.lower():
            ag["descricao"] = req.descricao
            ag["acoes"] = list(set(ag["acoes"] + req.acoes))
            ag["ultima_atualizacao"] = datetime.now().strftime("%Y-%m-%d")
            atualizado = True
            break

    if not atualizado:
        dados["agentes"].append({
            "nome_agente": req.nome_agente,
            "descricao": req.descricao,
            "acoes": req.acoes,
            "criado_em": datetime.now().strftime("%Y-%m-%d"),
            "ultima_atualizacao": datetime.now().strftime("%Y-%m-%d")
        })

    with open(caminho, "w", encoding="utf-8") as f:
        yaml.dump(dados, f, allow_unicode=True)

    return {
        "status": "Registro salvo",
        "agente": req.nome_agente,
        "total": len(dados["agentes"])
    }

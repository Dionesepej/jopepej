from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime
import yaml

app = FastAPI()

# ==== MODELOS ====
class TextoSimples(BaseModel):
    conteudo: str

class AgenteNovo(BaseModel):
    nome: str
    descricao: str
    acoes_usadas: List[str]

class PromptRequest(BaseModel):
    dominio: str
    estilo_resposta: str
    proposito: str

class BlueprintRequest(BaseModel):
    objetivo_diagnosticado: str

# ==== ROTAS GENÉRICAS SIMULADAS ====
@app.post("/criarPromptMatriz")
def criar_prompt(req: PromptRequest):
    return {"prompt": f"Você é um agente criado para {req.dominio}, com estilo {req.estilo_resposta}, para {req.proposito}."}

@app.post("/gerarBlueprintDoAgente")
def gerar_blueprint(req: BlueprintRequest):
    return {"blueprint": {"planner": "Analisa", "executor": "Executa", "reflexion_chain": True}}

@app.post("/registrar-agente")
def registrar_agente(req: AgenteNovo):
    caminho_arquivo = "registro_de_agentes.yaml"
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            registro = yaml.safe_load(f) or {}
    except FileNotFoundError:
        registro = {"agentes": []}

    atualizado = False
    for agente in registro["agentes"]:
        if agente["nome"].lower() == req.nome.lower():
            agente["descricao"] = req.descricao
            agente["acoes_usadas"] = list(set(agente["acoes_usadas"] + req.acoes_usadas))
            agente["data_atualizacao"] = datetime.now().strftime("%Y-%m-%d")
            atualizado = True
            break

    if not atualizado:
        registro["agentes"].append({
            "nome": req.nome,
            "descricao": req.descricao,
            "acoes_usadas": req.acoes_usadas,
            "data_criacao": datetime.now().strftime("%Y-%m-%d"),
            "observacoes": ""
        })

    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        yaml.dump(registro, f, allow_unicode=True)

    return {
        "status": "Agente registrado com sucesso.",
        "total_agentes": len(registro["agentes"])
    }

# ==== ROTAS MOCKADAS ====
@app.post("/{rota_personalizada}")
def rota_generica(rota_personalizada: str, body: Optional[Dict] = None):
    return {
        "mensagem": f"Ação '{rota_personalizada}' recebida com sucesso.",
        "entrada": body or {},
        "status": "simulado"
    }

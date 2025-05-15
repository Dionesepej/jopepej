from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime
import yaml
from acao_registrarHistoricoOmega import registrar_historico
from acao_observerOmega import observer

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

# ==== ROTAS UNIVERSAIS ====
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

@app.post("/criarPromptMatriz")
def criar_prompt(req: PromptRequest):
    return {
        "prompt": f"Você é um agente criado para {req.dominio}, com estilo {req.estilo_resposta}, para {req.proposito}."
    }

@app.post("/gerarBlueprintDoAgente")
def gerar_blueprint(req: BlueprintRequest):
    return {
        "blueprint": {
            "planner": "Analisa contexto e objetivos",
            "executor": "Executa plano de ação",
            "reflexion_chain": True
        }
    }

# ==== ROTAS INTELIGENTES DO GPT-SIGMA ====
@app.post("/segmentar_topicos")
def segmentar_topicos(req: TextoSimples):
    blocos = req.conteudo.split("\\n\\n")
    return {"topicos": blocos}

@app.post("/detectar_palavras_chave")
def detectar_keywords(req: TextoSimples):
    palavras = list(set(req.conteudo.lower().split()))
    return {"palavras_chave": palavras[:6]}

@app.post("/mapear_artigos_legais")
def mapear_artigos(req: TextoSimples):
    return {"artigos": ["Art. 5º CF", "Art. 37 CF"]}

@app.post("/extrair_jurisprudencia")
def extrair_juris(req: TextoSimples):
    return {"jurisprudencias": ["STF: Tema 123", "STJ: Súmula 456"]}

@app.post("/flashcard_builder")
def flashcard_builder(req: TextoSimples):
    return {"flashcards": [{"pergunta": "Defina um conceito chave", "resposta": "Simulado"}]}

@app.post("/quiz_generator")
def quiz_generator(req: TextoSimples):
    return {"quiz": [{"questao": "O que é devido processo legal?", "gabarito": "Garantia constitucional"}]}

@app.post("/summary_engine")
def summary_engine(req: TextoSimples):
    return {"resumo": req.conteudo[:120] + "..."}

@app.post("/reflexion_chain")
def reflexion_chain(req: TextoSimples):
    return {"ajuste": "Corrigida ausência de jurisprudência no bloco 2"}

@app.post("/self_diagnostic_module")
def self_diag(req: TextoSimples):
    return {"verificacao": "Bloco doutrinário ausente"}

@app.post("/validacao_rigorosa")
def validacao_rigorosa(req: TextoSimples):
    return {"validado": True}

# ==== ROTA UNIVERSAL ====
@app.post("/{rota_personalizada}")
def rota_generica(rota_personalizada: str, body: Optional[Dict] = None):
    return {
        "mensagem": f"Ação '{rota_personalizada}' recebida com sucesso.",
        "entrada": body or {},
        "status": "simulado"
    }

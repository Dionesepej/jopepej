from datetime import datetime
import yaml

def observer(nome_agente: str, acao: str, entrada: dict, saida: dict):
    caminho = "historico_execucao.yaml"
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            historico = yaml.safe_load(f) or []
    except FileNotFoundError:
        historico = []

    historico.append({
        "timestamp": datetime.now().isoformat(),
        "agente": nome_agente,
        "acao": acao,
        "entrada": entrada,
        "saida": saida
    })

    with open(caminho, "w", encoding="utf-8") as f:
        yaml.dump(historico, f, allow_unicode=True)

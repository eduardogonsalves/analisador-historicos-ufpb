from collections import defaultdict

SITUACOES = [
    "APROVADO", "REPROVADO", "REP. FALTA", "TRANCADO",
    "MATRICULADO", "EQUIVALÊNCIA", "DISPENSADO"
]

def contar_situacoes(registros):
    """
    Agrupa por disciplina e conta as situações.
    Retorna um dict: {codigo: {situacao: contagem, ...}, ...}
    """
    resultado = defaultdict(lambda: defaultdict(int))
    for reg in registros:
        codigo = reg["codigo"]
        situacao = reg["situacao"]
        # Normaliza situação para evitar erros de digitação
        situacao = situacao.upper()
        if situacao not in SITUACOES:
            if "REPROVADO" in situacao:
                situacao = "REPROVADO"
            elif "FALTA" in situacao:
                situacao = "REP. FALTA"
            elif "TRANCADO" in situacao:
                situacao = "TRANCADO"
            elif "MATRICULADO" in situacao:
                situacao = "MATRICULADO"
            elif "EQUIVALÊNCIA" in situacao:
                situacao = "EQUIVALÊNCIA"
            elif "DISPENSADO" in situacao:
                situacao = "DISPENSADO"
        resultado[codigo][situacao] += 1
        resultado[codigo]["total"] += 1
    return resultado
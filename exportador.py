import pandas as pd

def exportar_para_csv(nome_arquivo, contagem, nome_saida):
    """
    contagem: dict {codigo: {situacao: contagem, ...}, ...}
    """
    linhas = []
    for codigo, situacoes in contagem.items():
        linha = {
            "Nome do arquivo": nome_arquivo,
            "Código da disciplina": codigo,
            "Número total de tentativas": situacoes.get("total", 0)
        }
        # Adiciona todas as situações como colunas
        for sit in ["APROVADO", "REPROVADO", "REP. FALTA", "TRANCADO", "MATRICULADO", "EQUIVALÊNCIA", "DISPENSADO"]:
            linha[sit] = situacoes.get(sit, 0)
        linhas.append(linha)
    df = pd.DataFrame(linhas)
    df.to_csv(nome_saida, index=False)
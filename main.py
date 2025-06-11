import os
from extrator import extrair_texto_pdf, extrair_registros
from contador import contar_situacoes
from exportador import exportar_para_csv

PASTA = "historicos"
SAIDA = "resultado.csv"

def main():
    todos_resultados = []
    for arquivo in os.listdir(PASTA):
        if arquivo.lower().endswith(".pdf"):
            caminho = os.path.join(PASTA, arquivo)
            print(f"Processando {arquivo}...")
            texto = extrair_texto_pdf(caminho)
            registros = extrair_registros(texto)
            contagem = contar_situacoes(registros)
            # Adiciona resultado para cada disciplina desse arquivo
            for codigo, situacoes in contagem.items():
                linha = {
                    "Nome do arquivo": arquivo,
                    "Código da disciplina": codigo,
                    "Número total de tentativas": situacoes.get("total", 0),
                    "APROVADO": situacoes.get("APROVADO", 0),
                    "REPROVADO": situacoes.get("REPROVADO", 0),
                    "REP. FALTA": situacoes.get("REP. FALTA", 0),
                    "TRANCADO": situacoes.get("TRANCADO", 0),
                    "MATRICULADO": situacoes.get("MATRICULADO", 0),
                    "EQUIVALÊNCIA": situacoes.get("EQUIVALÊNCIA", 0),
                    "DISPENSADO": situacoes.get("DISPENSADO", 0),
                }
                todos_resultados.append(linha)
    # Exporta tudo junto
    import pandas as pd
    df = pd.DataFrame(todos_resultados)
    df.to_csv(SAIDA, index=False)
    print(f"Arquivo {SAIDA} gerado com sucesso.")

if __name__ == "__main__":
    main()
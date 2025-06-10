import fitz
import os
import pandas as pd

CODIGO_CALCULO_I = "1103177"
pasta = "historicos/"

def analisar_historico(pdf_path):
    doc = fitz.open(pdf_path)
    texto = ""
    for page in doc:
        texto += page.get_text()

    linhas = texto.split("\n")
    tentativas = []

    for linha in linhas:
        if CODIGO_CALCULO_I in linha:
            tentativas.append(linha.strip())
            print("DEBUG:", linha.strip())  # Ajuda na verificação visual

    # Agora vamos contar as situações
    def contar_situacao(chave):
        return sum(chave in l.upper() for l in tentativas)

    resultado = {
        "Arquivo": os.path.basename(pdf_path),
        "Tentativas": len(tentativas),
        "Aprovado": contar_situacao("APROVADO"),
        "Reprovado": contar_situacao("REPROVADO") - contar_situacao("REP. FALTA"),  # Exclusivo
        "Por Falta": contar_situacao("REP. FALTA"),
        "Trancado": contar_situacao("TRANCADO"),
        "Matriculado": contar_situacao("MATRICULADO"),
        "Equivalência": contar_situacao("EQUIVALÊNCIA"),
        "Dispensado": contar_situacao("DISPENSADO")
    }

    return resultado

# Processar todos os históricos da pasta
resultados = []
for arquivo in os.listdir(pasta):
    if arquivo.endswith(".pdf"):
        resultado = analisar_historico(os.path.join(pasta, arquivo))
        resultados.append(resultado)

# Gerar a planilha
df = pd.DataFrame(resultados)
df.to_csv("resultado_calculo1.csv", index=False)
print(df)

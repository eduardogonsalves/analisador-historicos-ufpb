import fitz  # PyMuPDF
import os

# Códigos das disciplinas de interesse
CODIGOS = [
    "1103118", "1103177", "1103178", "1103179", "1103180", "1103232"
]

def extrair_texto_pdf(caminho_pdf):
    texto = ""
    with fitz.open(caminho_pdf) as doc:
        for page in doc:
            texto += page.get_text()
    return texto

def extrair_registros(texto):
    """
    Retorna uma lista de dicionários com os campos extraídos das linhas das disciplinas de interesse.
    """
    registros = []
    linhas = texto.splitlines()
    for linha in linhas:
        for codigo in CODIGOS:
            if linha.strip().startswith(codigo):
                # Exemplo de linha:
                # 1103118 CÁLCULO VETORIAL E GEOMETRIA ANALÍTICA 60 OB 2022.2 03 0.0 REPROVADO
                partes = linha.split()
                if len(partes) < 8:
                    continue  # Linha incompleta
                # Pega o código, nome, situação, ano/sem
                codigo_disc = partes[0]
                nome_disc = " ".join(partes[1:-6])
                ano_sem = partes[-5]
                situacao = partes[-1]
                registros.append({
                    "codigo": codigo_disc,
                    "nome": nome_disc,
                    "ano_sem": ano_sem,
                    "situacao": situacao
                })
    return registros
import pdfplumber
import pandas as pd
from zipfile import ZipFile

nome_pdf = "pdfs/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
nome_csv = "Rol_de_Procedimentos.csv"
nome_zip = "Teste_Beatriz.zip"

tabelas = []

print("Extraindo tabelas do PDF")

with pdfplumber.open(nome_pdf) as pdf:
    for pag in pdf.pages:
        tabelas_extraidas = pag.extract_tables()
        for tabela in tabelas_extraidas:
            tabelas.extend(tabela)

dataframe = pd.DataFrame(tabelas)

dataframe.columns = dataframe.iloc[0]
dataframe = dataframe[1:]

dataframe.replace({"OD": "Odontológico", "AMB": "Ambulatorial"}, inplace=True)

dataframe.to_csv(nome_csv, index=False, encoding="utf-8")

with ZipFile(nome_zip, "w") as zipf:
    zipf.write(nome_csv)

print(f"Extração concluída! Arquivo salvo como {nome_zip}")

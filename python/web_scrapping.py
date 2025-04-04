import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

url_pagina = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

download_dir = "pdfs"
os.makedirs(download_dir, exist_ok=True)

retorno = requests.get(url_pagina)

soup = BeautifulSoup(retorno.text, "html.parser")
pdf_links = {}
for link in soup.find_all("a", href=True):
    href = link["href"]
    if "Anexo" in href and href.endswith(".pdf"):
        nome_pdf = href.split("/")[-1]
        pdf_links[nome_pdf] = href if href.startswith("http") else "https://www.gov.br" + href

for nome_arquivo, url in pdf_links.items():
    retorno = requests.get(url, stream=True)
    caminho_arquivo = os.path.join(download_dir, nome_arquivo)
    with open(caminho_arquivo, "wb") as file:
        for chunk in retorno.iter_content(1024):
            file.write(chunk)
        print(f"Baixado: {nome_arquivo}")

nome_arquivo_zip = "Anexos.zip"
with ZipFile(nome_arquivo_zip, "w") as zipf:
    for nome_arquivo in pdf_links.keys():
        caminho_arquivo = os.path.join(download_dir, nome_arquivo)
        zipf.write(caminho_arquivo, nome_arquivo)

print(f"Arquivos compactados em {nome_arquivo_zip}")

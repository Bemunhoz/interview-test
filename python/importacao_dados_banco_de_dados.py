import os
import mysql.connector
import glob
import pandas as pd

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="ans_db",
    allow_local_infile=True
)
cursor = conexao.cursor()

caminho_csv_contabeis = "dados/demonstracoes_contabeis/"
caminho_csv_operadoras = "dados/operadoras/"

arquivos_csv_contabeis = glob.glob(os.path.join(caminho_csv_contabeis, "*.csv"))
arquivos_csv_operadoras = glob.glob(os.path.join(caminho_csv_operadoras, "*.csv"))

for arquivo in arquivos_csv_contabeis:
    print(f"Importando {arquivo}...")
    df = pd.read_csv(arquivo, sep=';', encoding='utf-8')
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO demonstracoes_contabeis (
                registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro,
                cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante,
                regiao_de_comercializacao, data_registro_ans
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, tuple(row))
    conexao.commit()

for arquivo in arquivos_csv_operadoras:
    print(f"Importando {arquivo}...")
    df = pd.read_csv(arquivo, sep=';', encoding='utf-8')

    df['VL_SALDO_INICIAL'] = df['VL_SALDO_INICIAL'].str.replace(',', '.').astype(float)
    df['VL_SALDO_FINAL'] = df['VL_SALDO_FINAL'].str.replace(',', '.').astype(float)

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO operadoras (
                data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final
            ) VALUES (
                %s, %s, %s, %s, %s, %s
            )
        """, tuple(row))
    conexao.commit()

cursor.close()
conexao.close()

print("Importação concluída!")

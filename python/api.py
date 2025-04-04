from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv("dados/demonstracoes_contabeis/Relatorio_cadop.csv", sep=";", dtype=str)
df.fillna("", inplace=True)

@app.get("/buscar")
def buscar_operadoras(nomeFantasia: str = Query(..., min_length=3)):
    resultado = df[df["Nome_Fantasia"].str.contains(nomeFantasia, case=False, na=False)]
    return resultado.to_dict(orient="records")

uvicorn.run(app, port=8000)

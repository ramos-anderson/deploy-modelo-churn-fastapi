# main.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# 1. Instância do FastAPI
app = FastAPI(title="API de Predição de Churn", description="Uma API simples para prever o churn de clientes.")

# 2. Carregar o modelo salvo
# O modelo é carregado apenas uma vez, quando a aplicação inicia.
try:
    modelo = joblib.load('modelo_churn.pkl')
    print("Modelo carregado com sucesso.")
except FileNotFoundError:
    print("Erro: Arquivo 'modelo_churn.pkl' não encontrado. Execute o script de treinamento primeiro.")
    modelo = None

# 3. Definir o formato dos dados de entrada com Pydantic
# Isso garante que a API receba os dados no formato que o modelo espera.
class DadosCliente(BaseModel):
    tempo_contrato: int
    fatura_mensal: float

# 4. Criar o endpoint de predição
@app.post("/prever_churn/")
def prever_churn(dados: DadosCliente):
    """
    Recebe os dados de um cliente e retorna a previsão de churn.
    - **tempo_contrato**: meses de contrato do cliente.
    - **fatura_mensal**: valor em R$ da fatura mensal do cliente.
    """
    if modelo is None:
        return {"erro": "Modelo não foi carregado."}

    # Converte os dados de entrada para um DataFrame do Pandas
    dados_df = pd.DataFrame([dados.dict()])
    
    # Faz a predição
    previsao = modelo.predict(dados_df)
    probabilidade = modelo.predict_proba(dados_df)
    
    # Formata a resposta
    resultado_previsao = "Sim" if previsao[0] == 1 else "Não"
    probabilidade_churn = f"{probabilidade[0][1] * 100:.2f}%"

    # Retorna a previsão e a probabilidade em formato JSON
    return {
        "churn_previsto": resultado_previsao,
        "probabilidade_de_churn": probabilidade_churn
    }

# Endpoint raiz para um "Olá, Mundo" e teste de funcionamento
@app.get("/")
def read_root():
    return {"Olá": "Bem-vindo à API de Churn!"}
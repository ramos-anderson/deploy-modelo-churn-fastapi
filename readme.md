# API de Previsão de Churn com FastAPI e Scikit-Learn

![Status](https://img.shields.io/badge/status-concluído-green)
![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95-teal?logo=fastapi)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.2-orange?logo=scikit-learn)

Este projeto demonstra o **deploy** de um modelo de Machine Learning, levando-o do ambiente de desenvolvimento para uma **API REST funcional**. O objetivo é servir um modelo treinado para prever o churn de clientes, tornando-o consumível por outras aplicações (como um CRM ou um dashboard de front-end) via requisições HTTP.

Este é um projeto prático de **Engenharia de Machine Learning (MLOps)**.

---

## 🚀 Arquitetura da Solução

O projeto é dividido em dois componentes principais:

1.  **`treinamento_modelo.py`:** Um script que utiliza a `scikit-learn` para treinar um modelo de Regressão Logística. Após o treinamento, o modelo é serializado e salvo como um arquivo (`modelo_churn.pkl`).
2.  **`main.py`:** Uma API web construída com **FastAPI** que:
    *   Carrega o modelo treinado (`modelo_churn.pkl`) em memória ao ser iniciada.
    *   Expõe um endpoint `POST /prever_churn/` que aceita os dados de um novo cliente.
    *   Usa o modelo para gerar uma predição ("Sim" ou "Não") e a probabilidade de churn.
    *   Retorna a previsão em formato JSON.

---

## 🛠️ Tecnologias Utilizadas

*   **Python:** Linguagem principal.
*   **Scikit-learn:** Para treinamento do modelo de Machine Learning.
*   **Joblib:** Para serialização (salvar/carregar) do modelo.
*   **FastAPI:** Framework web de alta performance para a construção da API.
*   **Pydantic:** Para validação dos dados de entrada (schema da API).
*   **Uvicorn:** Servidor ASGI para executar a aplicação.

---

## ⚙️ Como Executar o Projeto Localmente

**1. Pré-requisitos:**
*   Ter o Python 3.9 (ou superior) instalado.

**2. Clone o repositório:**
git clone https://github.com/ramos-anderson/deploy-modelo-churn.git
cd deploy-modelo-churn

**3. Crie um ambiente virtual e instale as dependências:**
# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate

# Instale as bibliotecas
pip install -r requirements.txt

**4. Treine o modelo (apenas na primeira vez):**
python treinamento_modelo.py
(Este comando criará o arquivo modelo_churn.pkl)

**5. Inicie a API:**
uvicorn main:app --reload
O servidor estará rodando em http://127.0.0.1:8000.

---

# 📈 Como Testar a API via Swagger UI

O FastAPI gera uma documentação interativa automaticamente.
Com o servidor rodando, acesse http://127.0.0.1:8000/docs no seu navegador.
Clique no endpoint POST /prever_churn/ e em "Try it out".
No campo "Request body", insira os dados de um cliente para teste e clique em "Execute".

**Exemplo 1 (previsão de CHURN):**
JSON
{
  "tempo_contrato": 2,
  "fatura_mensal": 60
}

**Exemplo 2 (previsão de NÃO CHURN):**
code
JSON
{
  "tempo_contrato": 48,
  "fatura_mensal": 125
}
A previsão será retornada na seção "Response body" da interface.


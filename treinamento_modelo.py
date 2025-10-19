# treinamento_modelo.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

print("Gerando e preparando os dados...")
# Criando um dataset fictício simples para o exemplo
data = {
    'tempo_contrato': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 24, 36, 48],
    'fatura_mensal': [50, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125],
    'churn': [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 1 = Sim, 0 = Não
}
df = pd.DataFrame(data)

# Definindo as features (X) e o alvo (y)
X = df[['tempo_contrato', 'fatura_mensal']]
y = df['churn']

print("Treinando o modelo de Regressão Logística...")
# Treinando o modelo
modelo = LogisticRegression()
modelo.fit(X, y)

print("Salvando o modelo treinado em 'modelo_churn.pkl'...")
# Salvando o modelo treinado em um arquivo .pkl
joblib.dump(modelo, 'modelo_churn.pkl')

print("\nModelo treinado e salvo com sucesso!")
print("O arquivo 'modelo_churn.pkl' foi criado nesta pasta.")
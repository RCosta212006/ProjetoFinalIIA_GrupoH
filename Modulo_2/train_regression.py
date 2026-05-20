import os
import pandas as pd
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

pasta_atual = os.path.dirname(os.path.abspath(__file__))
pasta_projeto = os.path.dirname(pasta_atual)
caminho_csv = os.path.join(pasta_projeto,"processed_lisboa_porto_air_quality.csv")
caminho_metricas = os.path.join(pasta_atual, "metrics.csv")
caminho_modelo = os.path.join(pasta_atual, "melhor_modelo_regressao.pkl")

try:
    print("A carregar os dados para regressão...")
    df = pd.read_csv(caminho_csv, sep=';')
except FileNotFoundError:
    print(f"ERRO: Não encontrei o CSV em: {caminho_csv}")
    exit()

# 1. Preparação e Limpeza de Dados 

df.columns = df.columns.str.lower()

# Converter datetime e criar variáveis temporais
df['datetime'] = pd.to_datetime(df['datetime'], format='%d/%m/%y %H:%M')
df['hour'] = df['datetime'].dt.hour
df['day'] = df['datetime'].dt.day
df['month'] = df['datetime'].dt.month

# Lista de colunas usadas 
colunas_verificar = [
    'no2', 'pm10', 'pm2.5', 'o3', 'so2', 'temperature_c', 
    'humidity_percent', 'wind_speed_kmh', 'pressure_hpa', 
    'precipitation_mm', 'datetime'
]

# Remover linhas com valores nulos nestas colunas
df_clean = df.dropna(subset=colunas_verificar).copy()

features = [
    'pm10', 'pm2.5', 'o3', 'so2', 'temperature_c', 
    'humidity_percent', 'wind_speed_kmh', 'pressure_hpa', 
    'precipitation_mm', 'day', 'month', 'hour'
]

X = df_clean[features]
y = df_clean['no2']

print(f"Dataset limpo: {df_clean.shape[0]} linhas utilizadas para treinar.")

# Divisão Treino/Teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Pipelines de Pré-processamento e Treino (Sem imputação de dados)
pipeline_lin_reg = Pipeline([
    ('scaler', StandardScaler()),
    ('modelo', LinearRegression())
])

pipeline_rf_reg = Pipeline([
    ('scaler', StandardScaler()),
    ('modelo', RandomForestRegressor(random_state=42, n_estimators=100))
])

# 2. Treinar Modelos
print("A treinar Regressão Linear...")
pipeline_lin_reg.fit(X_train, y_train)
preds_lin_reg = pipeline_lin_reg.predict(X_test)

print("A treinar Random Forest Regressor...")
pipeline_rf_reg.fit(X_train, y_train)
preds_rf_reg = pipeline_rf_reg.predict(X_test)

# 3. Avaliar e Guardar Métricas
def avaliar_reg(nome, y_true, y_pred):
    return {
        'Modelo': nome,
        'Tarefa': 'Regressao (NO2)',
        'MAE': mean_absolute_error(y_true, y_pred),
        'RMSE': np.sqrt(mean_squared_error(y_true, y_pred)), 
        'R2': r2_score(y_true, y_pred)
    }

resultados_reg = [
    avaliar_reg('Regressao Linear', y_test, preds_lin_reg),
    avaliar_reg('Random Forest Regressor', y_test, preds_rf_reg)
]

df_nova_metrica = pd.DataFrame(resultados_reg)
print("\n=== Resultados da Regressão ===")
print(df_nova_metrica.to_string(index=False))

try:
    df_existente = pd.read_csv(caminho_metricas)
    df_final = pd.concat([df_existente, df_nova_metrica], ignore_index=True)
except FileNotFoundError:
    df_final = df_nova_metrica

df_final.to_csv(caminho_metricas, index=False)
print(f"\nMétricas atualizadas em {caminho_metricas}")

joblib.dump(pipeline_rf_reg, caminho_modelo)
print(f"Melhor modelo guardado em {caminho_modelo}")
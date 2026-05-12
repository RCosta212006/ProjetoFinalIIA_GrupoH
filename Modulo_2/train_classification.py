import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# 1. Definir os Caminhos
pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(pasta_atual, "processed_lisboa_porto_air_quality.csv")
caminho_metricas = os.path.join(pasta_atual, "metrics.csv")
caminho_modelo = os.path.join(pasta_atual, "melhor_modelo_classificacao.pkl")

# 2. Carregar os Dados
try:
    print("A carregar os dados...")
    df = pd.read_csv(caminho_csv, sep=';')
except FileNotFoundError:
    print(f"ERRO: Não encontrei o CSV em: {caminho_csv}")
    exit()

# 3. Preparação e Limpeza de Dados
# Passar para minúsculas para não haver erros
df.columns = df.columns.str.lower()

# Converter datetime e criar variáveis temporais
df['datetime'] = pd.to_datetime(df['datetime'])
df['hour'] = df['datetime'].dt.hour
df['day'] = df['datetime'].dt.day
df['month'] = df['datetime'].dt.month

# Remover as linhas com nulos APENAS nas colunas que vão ser usadas
colunas_para_verificar = ['datetime', 'temperature_c', 'humidity_percent', 'c6h6', 'air_quality_good']
df_clean = df.dropna(subset=colunas_para_verificar).copy()

# Definir as features e a variável alvo
features = ['temperature_c', 'humidity_percent', 'c6h6', 'hour', 'day', 'month']
X = df_clean[features]
y = df_clean['air_quality_good'].astype(int) # Converte True/False para 1/0

print(f"Dataset limpo: {df_clean.shape[0]} linhas utilizadas para treinar.")

# Divisão Treino/Teste (80% / 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 4. Pipelines de Pré-processamento e Treino (Sem imputação de dados)
pipeline_lr = Pipeline([
    ('scaler', StandardScaler()),
    ('modelo', LogisticRegression(max_iter=1000))
])

pipeline_rf = Pipeline([
    ('scaler', StandardScaler()),
    ('modelo', RandomForestClassifier(random_state=42, n_estimators=100))
])

# 5. Treinar os dois modelos
print("A treinar a Regressão Logística...")
pipeline_lr.fit(X_train, y_train)
preds_lr = pipeline_lr.predict(X_test)

print("A treinar o Random Forest Classifier...")
pipeline_rf.fit(X_train, y_train)
preds_rf = pipeline_rf.predict(X_test)

# 6. Avaliar e Guardar Métricas
def avaliar(nome, y_true, y_pred):
    return {
        'Modelo': nome,
        'Tarefa': 'Classificacao',
        'Accuracy': accuracy_score(y_true, y_pred),
        'Precision': precision_score(y_true, y_pred, zero_division=0),
        'Recall': recall_score(y_true, y_pred, zero_division=0),
        'F1-Score': f1_score(y_true, y_pred, zero_division=0)
    }

resultados = [
    avaliar('Regressao Logistica', y_test, preds_lr),
    avaliar('Random Forest Classifier', y_test, preds_rf)
]

df_resultados = pd.DataFrame(resultados)
print("\n=== Resultados da Classificação ===")
print(df_resultados.to_string(index=False))

# Guardar os resultados no CSV
df_resultados.to_csv(caminho_metricas, index=False)
print(f"\nMétricas guardadas em {caminho_metricas}")

# Guardar o melhor modelo 
joblib.dump(pipeline_rf, caminho_modelo)
print(f"Melhor modelo guardado em {caminho_modelo}")
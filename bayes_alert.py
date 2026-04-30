import pandas as pd
import sys

# Cria uma função para calcular a probabilidade de um evento -> Default é True
def probabilidade_evento(df, coluna, valor=True):
    # Compara cada linha com o valor pretendido
    return (df[coluna] == valor).mean() 

    # df["Calor"] == True
    # O .mean() calcula a proporção de valores verdadeiros
    # Se 30 em 100 linhas forem True, dá 0.30. 
    # 30 / 100 (30 valores True e divide-se por o número de linhas)

# Exemplo : P(Incendio | Calor=True) = ?

# Incendio | Calor | Vento | Poluicao
# -----------------------------------
# True     | True  | True  | False
# False    | True  | False | False

def probabilidade_condicional(df, evento, evidencia):
    subconjunto = df.copy()

    for coluna, valor in evidencia.items():
        subconjunto = subconjunto[subconjunto[coluna] == valor] # Só as linhas que queres da evidência

    if len(subconjunto) == 0:
        return 0

    # Vai comparar 
    # True
    # False

    # .mean()
    # (1 + 0) / 2 = 0.5

    return (subconjunto[evento] == True).mean() # P(Incendio | Calor=True) = 0.5


# Exemplo de variáveis bayes 

# Incendio | Calor | Vento | Poluicao
# -----------------------------------
# True     | True  | True  | False
# False    | False | False | False
# False    | False | False | False
# False    | False | False | True
# False    | True  | False | False

def preparar_variaveis_bayes(df):
    df_bayes = pd.DataFrame()

    df_bayes["Incendio"] = df["alertas"].str.contains("risco_incendio_alto", na=False)
    df_bayes["Calor"] = df["alertas"].str.contains("risco_calor_extremo|risco_incendio_alto", na=False)
    df_bayes["Vento"] = df["alertas"].str.contains("vento_forte", na=False)
    df_bayes["Poluicao"] = df["alertas"].str.contains( "poluicao_no2_alta|particulas_pm10_altas|particulas_pm25_altas|ozono_alto",na=False)

    return df_bayes


def inferencia_por_enumeracao(df_bayes):
    resultados = {
        "P(Calor)": probabilidade_evento(df_bayes, "Calor"),
        "P(Vento)": probabilidade_evento(df_bayes, "Vento"),
        "P(Poluicao)": probabilidade_evento(df_bayes, "Poluicao"),
        "P(Incendio)": probabilidade_evento(df_bayes, "Incendio"),
        "P(Incendio | Calor=True)": probabilidade_condicional( df_bayes,"Incendio",{"Calor": True}),
        "P(Incendio | Calor=True, Vento=True)": probabilidade_condicional(df_bayes,"Incendio",{"Calor": True, "Vento": True}),
        "P(Poluicao | Calor=True)": probabilidade_condicional(df_bayes,"Poluicao",{"Calor": True})
    }

    return resultados


def main(alert_csv):
    df = pd.read_csv(alert_csv)

    df_bayes = preparar_variaveis_bayes(df)
    resultados = inferencia_por_enumeracao(df_bayes)

    print("Resultados da Rede Bayesiana baseada nos alertas:\n")

    for chave, valor in resultados.items():
        print(f"{chave}: {valor:.3f}")


if __name__ == "__main__":
    ficheiro = sys.argv[1] if len(sys.argv) > 1 else "alert_results.csv"
    main(ficheiro)
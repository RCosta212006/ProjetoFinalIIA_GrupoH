import pandas as pd
import sys


def sistema_de_regras(row):
    alertas = []
    acoes = []

    # Vai buscar o valor da coluna associada, se não existir coloca como 0
    temp = row.get("temperature_c", 0)
    humidade = row.get("humidity_percent", 0)
    vento = row.get("wind_speed_kmh", 0)
    precipitacao = row.get("precipitation_mm", 0)

    no2 = row.get("NO2", 0)
    pm10 = row.get("PM10", 0)
    pm25 = row.get("PM2.5", 0)
    o3 = row.get("O3", 0)

    # Regras -> Adiciona o alerta na lista de alertas e a ação associada à lista de ações
    if temp > 40 and humidade < 20:
        alertas.append("risco_incendio_alto")
        acoes.append("Activar meios de vigilância e prevenção de incêndios")

    elif temp > 35 and humidade < 30:
        alertas.append("risco_calor_extremo")
        acoes.append("Emitir aviso de calor à população")

    if precipitacao > 30:
        alertas.append("risco_inundacao")
        acoes.append("Monitorizar zonas baixas e linhas de água")

    if vento > 60:
        alertas.append("vento_forte")
        acoes.append("Recomendar evitar zonas arborizadas")

    if no2 > 100:
        alertas.append("poluicao_no2_alta")
        acoes.append("Reduzir tráfego em zonas críticas")

    if pm10 > 50:
        alertas.append("particulas_pm10_altas")
        acoes.append("Avisar população sensível")

    if pm25 > 25:
        alertas.append("particulas_pm25_altas")
        acoes.append("Recomendar uso de máscara a grupos vulneráveis")

    if o3 > 120:
        alertas.append("ozono_alto")
        acoes.append("Evitar exercício físico ao ar livre")

    if temp < 5:
        alertas.append("frio_extremo")
        acoes.append("Activar apoio a população vulnerável")

    if humidade > 90 and temp < 10:
        alertas.append("risco_nevoeiro")
        acoes.append("Emitir aviso para condução prudente")

    if not alertas:
        alertas.append("sem_alerta")
        acoes.append("Sem acção necessária")

    # Os alertas todos juntos numa só string e as ações todas juntas numa só string.
    return "; ".join(alertas), "; ".join(acoes)


# Cria a função principal do programa
def main(input_csv):
    df = pd.read_csv(input_csv, sep=";")

    # Cria uma cópia da tabela original
    # Assim, o programa mantém os dados originais e acrescenta novas colunas
    resultados = df.copy()

    # Cria duas novas colunas: alerta e acoes_recomendadas
    # Aplica a função sistema_de_regras a cada linha
    # Como a função devolve duas coisas, pd.Series permite colocá-las em duas colunas diferentes
    resultados[["alertas", "acoes_recomendadas"]] = resultados.apply(
        lambda row: pd.Series(sistema_de_regras(row)),
        axis=1
    )

    # Grava a tabela final no ficheiro alert_results.csv.
    resultados.to_csv("alert_results.csv", index=False)
    print("Ficheiro alert_results.csv criado com sucesso.")


if __name__ == "__main__":
    ficheiro = sys.argv[1] if len(sys.argv) > 1 else "processed_lisboa_porto_air_quality.csv"
    main(ficheiro)
# Este ficheiro vai:
# - Definir regras;
# - Aplicar regras ao dataset;
# - Gerar riscos e acções;

import pandas as pd

# Função responsável pela verificação de dados inexistentes
def has_values(row, columns):
    return all(pd.notna(row[col]) for col in columns)

#Vai substituir o ficheiro regras.json
def load_rules():
    return [

        # ----------- Regras baseadas em incêndio, calor e propagação -----------

        # Risco de incêndio alto
        # Muito calor + pouca humidade → vegetação seca → risco alto
        {
            "name": "fire_high",
            "condition": lambda row: has_values(row, ["temperature_c", "humidity_percent"]) and row["temperature_c"] > 40 and row["humidity_percent"] < 20,
            "risk": "Risco de incêndio alto",
            "priority": "critica",
            "action": "Emitir alerta máximo e activar meios de combate a incêndios."
        },

        # Risco de propagação rápida de incêndio
        # Calor + humidade baixa + vento
        {
            "name": "fire_spread",
            "condition": lambda row: has_values(row, ["temperature_c", "humidity_percent", "wind_speed_kmh"])
                            and row["temperature_c"] > 30
                            and row["humidity_percent"] < 35
                            and row["wind_speed_kmh"] > 20,
            "risk": "Elevado risco de propagação de incêndio",
            "priority": "critica",
            "action": "Preparar meios de contenção e reforçar vigilância."
        },

        # Calor extremo
        {
            "name": "extreme_heat",
            "condition": lambda row: has_values(row, ["temperature_c"]) and row["temperature_c"] > 38,
            "risk": "Calor extremo",
            "priority": "alta",
            "action": "Avisar grupos vulneráveis e activar medidas preventivas."
        },
        
        # ----------- Regras baseadas em precipitação e vento -----------

        # Precipitação intensa
        {
            "name": "heavy_rain",
            "condition": lambda row: has_values(row, ["precipitation_mm"]) and row["precipitation_mm"] >= 10,
            "risk": "Precipitação intensa",
            "priority": "alta",
            "action": "Monitorizar zonas urbanas com risco de inundação."
        },

        # Precipitação muito intensa
        {
            "name": "very_heavy_rain",
            "condition": lambda row: has_values(row, ["precipitation_mm"]) and row["precipitation_mm"] >= 20,
            "risk": "Precipitação muito intensa",
            "priority": "critica",
            "action": "Reforçar alerta de inundação e activar prevenção local."
        },

        # Vento forte
        {
            "name": "strong_wind",
            "condition": lambda row: has_values(row, ["wind_speed_kmh"]) and row["wind_speed_kmh"] >= 20,
            "risk": "Vento forte",
            "priority": "media",
            "action": "Avisar serviços municipais e monitorizar estruturas expostas."
        },

        # Tempestade local
        {
            "name": "local_storm_risk",
            "condition": lambda row: has_values(row, ["precipitation_mm", "wind_speed_kmh"]) and row["precipitation_mm"] >= 10 and row["wind_speed_kmh"] >= 20,
            "risk": "Risco de tempestade local",
            "priority": "alta",
            "action": "Emitir alerta meteorológico local e reforçar prevenção."
        },

        # ----------- Regras baseadas em qualidade do ar -----------

        # Poluição por PM2.5
        {
            "name": "pm25_high",
            "condition": lambda row: has_values(row, ["PM2.5"]) and row["PM2.5"] > 25,
            "risk": "Poluição elevada por PM2.5",
            "priority": "alta",
            "action": "Recomendar redução de exposição ao ar livre."
        },

        # Poluição por PM10
        {
            "name": "pm10_high",
            "condition": lambda row: has_values(row, ["PM10"]) and row["PM10"] > 45,
            "risk": "Poluição elevada por PM10",
            "priority": "media",
            "action": "Recomendar precaução respiratória a grupos sensíveis."
        },

        # NO2 elevado
        {
            "name": "no2_high",
            "condition": lambda row: has_values(row, ["NO2"]) and row["NO2"] > 200,
            "risk": "Poluição elevada por NO2",
            "priority": "alta",
            "action": "Emitir aviso de qualidade do ar."
        },

        # O3 elevado
        {
            "name": "o3_high",
            "condition": lambda row: has_values(row, ["O3"]) and row["O3"] > 100,
            "risk": "Ozono troposférico elevado",
            "priority": "media",
            "action": "Alertar grupos vulneráveis para evitar esforço físico no exterior."
        },

        # ----------- Regras híbridas -----------

        # Calor extremo + PM2.5 elevado
        {
            "name": "heat_pm25_combined",
            "condition": lambda row: has_values(row, ["temperature_c", "PM2.5"]) and row["temperature_c"] > 35 and row["PM2.5"] > 25,
            "risk": "Calor extremo com poluição por PM2.5",
            "priority": "critica",
            "action": "Alertar população vulnerável e restringir exposição exterior."
        },

        # Incêndio com vento
        {
            "name": "fire_wind_critical",
            "condition": lambda row: has_values(row, ["temperature_c", "humidity_percent", "wind_speed_kmh"]) and row["temperature_c"] > 35 and row["humidity_percent"] < 30 and row["wind_speed_kmh"] >= 36,
            "risk": "Risco crítico de incêndio com vento forte",
            "priority": "critica",
            "action": "Activar plano de emergência local."
        }
    ]


def infer_row(row, rules):
    """
    Aplica todas as regras a uma linha do dataset.
    Se a condição de uma regra for verdadeira, essa regra é activada.
    """

    matched_rules = []

    for rule in rules:
        try:
            if rule["condition"](row):
                matched_rules.append(rule)
        except Exception as error:
            print(f"Erro ao avaliar a regra {rule['name']}: {error}")

    return matched_rules

# Decide qual o risco mais importante
def highest_priority(rules):
    """
    Recebe a lista de regras que foram activadas para uma determinada linha
    e devolve a prioridade mais elevada encontrada.
    """

    # Se nenhuma regra foi activada, não existe prioridade
    if not rules:
        return "nenhuma"

    # Mapeamento das prioridades para valores numéricos
    # Isto permite comparar prioridades facilmente
    priority_order = {
        "baixa": 1,
        "media": 2,
        "alta": 3,
        "critica": 4
    }

    # Procura a regra com maior prioridade
    highest = max(rules, key=lambda rule: priority_order[rule["priority"]])

    return highest["priority"]

# Lê o CSV e aplica as regras a todas as linhas
def process_dataset(file_path):
    """
    Lê o ficheiro CSV, aplica o motor de inferência a cada linha
    e devolve um novo DataFrame com os riscos detectados e acções recomendadas.
    """

    # Leitura do dataset
    # O ficheiro usa separador ';'
    df = pd.read_csv(file_path, sep=";")

    # Carrega a base de conhecimento
    rules = load_rules()

    # Lista onde vão ser guardados os resultados finais
    outputs = []

    # Percorre cada linha do dataset
    for _, row in df.iterrows():

        # Aplica as regras à linha actual
        matched_rules = infer_row(row, rules)

        # Extrai os nomes dos riscos detectados
        risks = [rule["risk"] for rule in matched_rules]

        # Extrai as acções recomendadas
        actions = [rule["action"] for rule in matched_rules]

        # Extrai os nomes técnicos das regras activadas
        rule_names = [rule["name"] for rule in matched_rules]

        # Guarda o resultado desta linha
        outputs.append({
            "city": row["city"],
            "datetime": row["datetime"],
            "matched_rules": " | ".join(rule_names) if rule_names else "Nenhuma",
            "detected_risks": " | ".join(risks) if risks else "Nenhum risco detectado",
            "recommended_actions": " | ".join(actions) if actions else "Sem acção recomendada",
            "priority": highest_priority(matched_rules)
        })

    # Converte os resultados para DataFrame
    return pd.DataFrame(outputs)

# Corre o programa
if __name__ == "__main__":
    # Nome do ficheiro de entrada
    input_file = r"C:\Users\rodri\OneDrive\Desktop\ProjetoFinalIIA\ProjetoFinalIIA_GrupoH\processed_lisboa_porto_air_quality.csv"

    # Nome do ficheiro de saída
    output_file = "alert_results.csv"

    # Processa o dataset
    result_df = process_dataset(input_file)

    # Mostra as primeiras linhas no terminal
    print(result_df.head(10))

    # Guarda os resultados num novo CSV
    result_df.to_csv(output_file, index=False)

    print(f"\nProcessamento concluído. Resultados guardados em: {output_file}")
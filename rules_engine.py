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


    ]


def infer_row(row, rules):
    matched_rules = []

    for rule in rules:
        if rule["condition"](row):
            matched_rules.append(rule)

    return matched_rules

# Decide qual o risco mais importante
def highest_priority(rules):
    ...

# Lê o CSV e aplica as regras a todas as linhas
def process_dataset(file_path):
    ...

# Corre o programa
if __name__ == "__main__":
    ...
"""
bayes_alerts.py

Rede Bayesiana simples para modelar incerteza no risco de incêndio.

Enquanto o ficheiro rules_engine.py usa regras determinísticas do tipo:
    SE temperatura > 40 E humidade < 20 -> risco de incêndio alto

este ficheiro usa probabilidades para responder a perguntas como:
    Qual é a probabilidade de haver risco de incêndio,
    sabendo que há calor extremo, baixa humidade e vento forte?
"""

from itertools import product


# ---------------------------------------------------------
# Definição da Rede Bayesiana
# ---------------------------------------------------------

# calor + pouca humidade + vento → maior probabilidade de incêndio

# Ordem dos nós da rede
VARIABLES = [
    "HeatExtreme",
    "LowHumidity",
    "StrongWind",
    "FireRisk"
]

# O calor extremo não depende de outro nó
# A humidade baixa não depende de outro nó
# O vento forte não depende de outro nó

#HeatExtreme ─┐
#LowHumidity ─┼──> FireRisk
#StrongWind  ─┘

# Pais de cada nó
PARENTS = {
    "HeatExtreme": [],
    "LowHumidity": [],
    "StrongWind": [],
    "FireRisk": ["HeatExtreme", "LowHumidity", "StrongWind"]
}


# Tabela de Probabilidades Condicionais
CPT = {
    # Probabilidades a priori
    # P(HeatExtreme=True)
    "HeatExtreme": {
        (): 0.20
    },

    # P(LowHumidity=True)
    "LowHumidity": {
        (): 0.30
    },

    # P(StrongWind=True)
    "StrongWind": {
        (): 0.25
    },

    # Probabilidade condicional:
    # P(FireRisk=True | HeatExtreme, LowHumidity, StrongWind)
    "FireRisk": {
        (True, True, True): 0.95,
        (True, True, False): 0.85,
        (True, False, True): 0.70,
        (True, False, False): 0.45,
        (False, True, True): 0.65,
        (False, True, False): 0.40,
        (False, False, True): 0.30,
        (False, False, False): 0.05
    }
}


# ---------------------------------------------------------
# Funções auxiliares da Rede Bayesiana
# ---------------------------------------------------------

# Esta função calcula a probabilidade de uma variável ter um certo valor
def probability(variable, value, evidence):
    """
    Devolve a probabilidade de uma variável ter determinado valor,
    tendo em conta a evidência já conhecida.

    Exemplo:
        probability("FireRisk", True, {
            "HeatExtreme": True,
            "LowHumidity": True,
            "StrongWind": False
        })
    """

    parents = PARENTS[variable]

    # Obtém os valores dos pais da variável
    parent_values = tuple(evidence[parent] for parent in parents)

    # Probabilidade de a variável ser True
    prob_true = CPT[variable][parent_values]

    # Se queremos P(variável=True), devolvemos prob_true
    if value is True:
        return prob_true

    # Se queremos P(variável=False), devolvemos 1 - prob_true
    return 1 - prob_true


def enumerate_all(variables, evidence):
    """
    Implementa inferência por enumeração.

    Esta função percorre todas as combinações possíveis das variáveis
    desconhecidas e soma as probabilidades compatíveis com a evidência.
    """

    # Caso base: se já não há variáveis, a probabilidade é 1
    if not variables:
        return 1.0

    first = variables[0]
    rest = variables[1:]

    # Se a variável já é conhecida pela evidência,
    # usamos directamente o seu valor
    if first in evidence:
        prob = probability(first, evidence[first], evidence)
        return prob * enumerate_all(rest, evidence)

    # Se a variável não é conhecida, somamos os dois casos:
    # variável=True e variável=False
    total = 0.0

    for value in [True, False]:
        extended_evidence = evidence.copy()
        extended_evidence[first] = value

        prob = probability(first, value, extended_evidence)
        total += prob * enumerate_all(rest, extended_evidence)

    return total


def query(query_variable, evidence):
    """
    Calcula a distribuição de probabilidade de uma variável.

    Exemplo:
        query("FireRisk", {
            "HeatExtreme": True,
            "LowHumidity": True
        })

    Devolve:
        {
            True: probabilidade de FireRisk=True,
            False: probabilidade de FireRisk=False
        }
    """

    result = {}

    # Calcula a probabilidade para True e False
    for value in [True, False]:
        extended_evidence = evidence.copy()
        extended_evidence[query_variable] = value

        result[value] = enumerate_all(VARIABLES, extended_evidence)

    # Normalização
    total = result[True] + result[False]

    result[True] = result[True] / total
    result[False] = result[False] / total

    return result


# ---------------------------------------------------------
# Conversão de dados meteorológicos em evidência booleana
# ---------------------------------------------------------

def build_evidence_from_weather(temperature_c, humidity_percent, wind_speed_kmh):
    """
    Converte valores numéricos semelhantes aos usados no rules_engine.py
    em evidência booleana para a Rede Bayesiana.

    Esta função faz a ponte entre o dataset e a Rede Bayesiana.
    """

    evidence = {
        "HeatExtreme": temperature_c > 38,
        "LowHumidity": humidity_percent < 30,
        "StrongWind": wind_speed_kmh >= 20
    }

    return evidence


def fire_risk_from_weather(temperature_c, humidity_percent, wind_speed_kmh):
    """
    Calcula a probabilidade de risco de incêndio com base em valores
    meteorológicos concretos.
    """

    evidence = build_evidence_from_weather(
        temperature_c,
        humidity_percent,
        wind_speed_kmh
    )

    result = query("FireRisk", evidence)

    return result


# ---------------------------------------------------------
# Exemplo de execução
# ---------------------------------------------------------

if __name__ == "__main__":

    # Exemplo semelhante às regras do rules_engine.py:
    # temperatura alta, humidade baixa e vento elevado
    temperature_c = 39
    humidity_percent = 25
    wind_speed_kmh = 22

    evidence = build_evidence_from_weather(
        temperature_c,
        humidity_percent,
        wind_speed_kmh
    )

    result = query("FireRisk", evidence)

    print("Evidência observada:")
    print(evidence)

    print("\nResultado da inferência Bayesiana:")
    print(f"P(FireRisk=True) = {result[True]:.2f}")
    print(f"P(FireRisk=False) = {result[False]:.2f}")

    print("Demonstração de uso de inferência por enumeração:")
    print(query("FireRisk", {"HeatExtreme": True}))
    print(query("FireRisk", {"HeatExtreme": True, "LowHumidity": True}))
    print(query("FireRisk", {"HeatExtreme": True, "LowHumidity": True, "StrongWind": True}))
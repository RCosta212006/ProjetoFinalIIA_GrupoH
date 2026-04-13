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
        {...},  # regra 1
        {...},  # regra 2
        ...
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
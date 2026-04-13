import pandas as pd

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

def highest_priority(rules):
    ...

def process_dataset(file_path):
    ...

if __name__ == "__main__":
    ...
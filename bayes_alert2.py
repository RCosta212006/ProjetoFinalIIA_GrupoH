import pandas as pd
import sys
from itertools import product


# ─────────────────────────────────────────────
# 1. Discretização dos dados ambientais
# ─────────────────────────────────────────────

def discretizar(df):
    d = pd.DataFrame()

    d["temp"] = pd.cut(df["temperature_c"],bins=[-50, 5, 25, 35, 60],labels=["frio", "normal", "quente", "extremo"])
    d["humidade"] = pd.cut(df["humidity_percent"],bins=[0, 30, 60, 80, 100],labels=["baixa", "normal", "alta", "muito_alta"])
    d["vento"] = pd.cut(df["wind_speed_kmh"],bins=[0, 20, 40, 60, 300],labels=["fraco", "moderado", "forte", "extremo"])
    d["pm10"] = pd.cut(df["PM10"],bins=[0, 25, 50, 100, 1000],labels=["boa", "moderada", "ma", "perigosa"])
    d["no2"] = pd.cut(df["NO2"],bins=[0, 40, 100, 200, 1000],labels=["baixo", "moderado", "alto", "muito_alto"])
    d["o3"] = pd.cut(df["O3"],bins=[0, 60, 120, 180, 1000],labels=["baixo", "moderado", "alto", "muito_alto"])

    # Variáveis alvo criadas a partir da coluna alertas
    d["incendio"] = df["alertas"].str.contains("risco_incendio_alto|risco_incendio_moderado", na=False).map({True: "sim", False: "nao"})
    d["poluicao"] = df["alertas"].str.contains("poluicao_no2_alta|particulas_pm10_altas|particulas_pm25_altas|ozono_alto",na=False).map({True: "sim", False: "nao"})

    return d.dropna()


# ─────────────────────────────────────────────
# 2. Classe da Rede Bayesiana
# ─────────────────────────────────────────────

class BayesianNetwork:
    """
    Rede Bayesiana discreta implementada de raiz.

    Estrutura da rede:

        temp ───────→ incendio
        humidade ───→ incendio
        vento ──────→ incendio

        pm10 ───────→ poluicao
        no2 ────────→ poluicao
        o3 ─────────→ poluicao
        incendio ───→ poluicao
    """

    def __init__(self):
        self.cpds = {}

        self.parents = {
            "temp": [],
            "humidade": [],
            "vento": [],
            "pm10": [],
            "no2": [],
            "o3": [],

            "incendio": ["temp", "humidade", "vento"],
            "poluicao": ["pm10", "no2", "o3", "incendio"]
        }

        self.categories = {}

    def fit(self, df, alpha=1.0):
    
        #Estima as CPDs através de frequências observadas, usando suavização de Laplace.    

        for node in self.parents:
            if hasattr(df[node], "cat"):
                self.categories[node] = list(df[node].cat.categories)
            else:
                self.categories[node] = list(df[node].unique())

            self.categories[node] = [str(v) for v in self.categories[node]]

        for node, pais in self.parents.items():
            vals_node = self.categories[node]
            self.cpds[node] = {}

            if not pais:
                counts = df[node].astype(str).value_counts()
                total = counts.sum() + alpha * len(vals_node)

                self.cpds[node][()] = {
                    v: (counts.get(v, 0) + alpha) / total
                    for v in vals_node
                }

            else:
                vals_pais = [self.categories[p] for p in pais]

                for combo_pais in product(*vals_pais):
                    mask = pd.Series([True] * len(df), index=df.index)

                    for p, v in zip(pais, combo_pais):
                        mask &= df[p].astype(str) == str(v)

                    subset = df[mask][node].astype(str)
                    counts = subset.value_counts()
                    total = counts.sum() + alpha * len(vals_node)

                    self.cpds[node][combo_pais] = {
                        v: (counts.get(v, 0) + alpha) / total
                        for v in vals_node
                    }

        print("CPDs estimadas com sucesso")
        return self

    def p_prior(self, node, value):
        
        #Calcula P(node=value) para nós sem pais.
        return self.cpds[node][()].get(str(value), 0)

    def p_cond(self, node, value, evidence):
        
        #Calcula P(node=value | pais).
        pais = self.parents[node]

        if not pais:
            return self.p_prior(node, value)

        key = tuple(str(evidence.get(p, "")) for p in pais)

        return self.cpds[node].get(key, {}).get(str(value), 1e-9)

    def query_incendio(self, temp=None, humidade=None, vento=None):
        """
        Calcula P(incendio | evidências).
        """

        evidence = {
            k: v for k, v in {
                "temp": temp,
                "humidade": humidade,
                "vento": vento
            }.items()
            if v is not None
        }

        probs = {}

        for inc in self.categories["incendio"]:
            if all(p in evidence for p in self.parents["incendio"]):
                prob = self.p_cond("incendio", inc, evidence)
            else:
                prob = 0.0

                temp_vals = [evidence["temp"]] if "temp" in evidence else self.categories["temp"]
                hum_vals = [evidence["humidade"]] if "humidade" in evidence else self.categories["humidade"]
                vento_vals = [evidence["vento"]] if "vento" in evidence else self.categories["vento"]

                for t, h, v in product(temp_vals, hum_vals, vento_vals):
                    ev = {
                        "temp": t,
                        "humidade": h,
                        "vento": v
                    }

                    prob += (
                        self.p_prior("temp", t)
                        * self.p_prior("humidade", h)
                        * self.p_prior("vento", v)
                        * self.p_cond("incendio", inc, ev)
                    )

            probs[inc] = prob

        total = sum(probs.values())

        if total > 0:
            probs = {k: v / total for k, v in probs.items()}

        return probs

    def query_poluicao(self, pm10=None, no2=None, o3=None, incendio=None):
        
        #Calcula P(poluicao | evidências).

        evidence = {
            k: v for k, v in {
                "pm10": pm10,
                "no2": no2,
                "o3": o3,
                "incendio": incendio
            }.items()
            if v is not None
        }

        probs = {}

        for pol in self.categories["poluicao"]:
            if all(p in evidence for p in self.parents["poluicao"]):
                prob = self.p_cond("poluicao", pol, evidence)
            else:
                prob = 0.0

                pm10_vals = [evidence["pm10"]] if "pm10" in evidence else self.categories["pm10"]
                no2_vals = [evidence["no2"]] if "no2" in evidence else self.categories["no2"]
                o3_vals = [evidence["o3"]] if "o3" in evidence else self.categories["o3"]
                inc_vals = [evidence["incendio"]] if "incendio" in evidence else self.categories["incendio"]

                for p10, n2, oz, inc in product(pm10_vals, no2_vals, o3_vals, inc_vals):
                    ev = {
                        "pm10": p10,
                        "no2": n2,
                        "o3": oz,
                        "incendio": inc
                    }

                    prob += (self.p_prior("pm10", p10) * self.p_prior("no2", n2) * self.p_prior("o3", oz) * self.p_cond("incendio", inc, {"temp": "quente", "humidade": "baixa", "vento": "forte"}) * self.p_cond("poluicao", pol, ev))

            probs[pol] = prob

        total = sum(probs.values())

        if total > 0:
            probs = {k: v / total for k, v in probs.items()}

        return probs

    def mostrar_cpds(self):
        
        #Mostra as CPDs estimadas.

        print("\nCPDs da Rede Bayesiana:\n")

        for node, tabela in self.cpds.items():
            print(f"--- {node} ---")

            for pais, probs in tabela.items():
                if pais == ():
                    print(f"P({node}) = {probs}")
                else:
                    print(f"P({node} | {pais}) = {probs}")

            print()


# ─────────────────────────────────────────────
# 3. Output
# ─────────────────────────────────────────────

def formatar_probabilidades(resultado):
    linhas = []

    for classe, prob in resultado.items():
        percentagem = prob * 100
        linhas.append(f"  - {classe}: {percentagem:.2f}%")

    return "\n".join(linhas)


def mostrar_consulta(titulo, resultado):
    print("\n" + "=" * 60)
    print(titulo)
    print("-" * 60)
    print(formatar_probabilidades(resultado))


# ─────────────────────────────────────────────
# 4. Execução principal
# ─────────────────────────────────────────────

def main(alert_csv):
    df = pd.read_csv(alert_csv)

    df_disc = discretizar(df)

    print("\n" + "=" * 60)
    print("REDE BAYESIANA — GESTÃO DE RISCOS AMBIENTAIS")
    print("=" * 60)

    print("\nDistribuição de categorias após discretização:")
    print("-" * 60)

    for col in df_disc.columns:
        print(f"\n{col.upper()}")

        contagens = df_disc[col].astype(str).value_counts()
        total = contagens.sum()

        for categoria, contagem in contagens.items():
            percentagem = (contagem / total) * 100
            print(f"  - {categoria}: {contagem} casos ({percentagem:.2f}%)")

    print("\n" + "=" * 60)
    print("A treinar Rede Bayesiana...")
    print("=" * 60)

    bn = BayesianNetwork()
    bn.fit(df_disc)

    print("\n" + "=" * 60)
    print("CONSULTAS DE INFERÊNCIA")
    print("=" * 60)

    mostrar_consulta(
        "P(incendio | temp=extremo, humidade=baixa, vento=forte)",
        bn.query_incendio(
            temp="extremo",
            humidade="baixa",
            vento="forte"
        )
    )

    mostrar_consulta(
        "P(incendio | temp=quente)",
        bn.query_incendio(
            temp="quente"
        )
    )

    mostrar_consulta(
        "P(incendio | temp=quente, humidade=baixa, vento=moderado)",
        bn.query_incendio(
            temp="quente",
            humidade="baixa",
            vento="moderado"
        )
    )

    mostrar_consulta(
        "P(poluicao | pm10=ma, no2=moderado, o3=moderado, incendio=sim)",
        bn.query_poluicao(
            pm10="ma",
            no2="moderado",
            o3="moderado",
            incendio="sim"
        )
    )

    mostrar_consulta(
        "P(poluicao | incendio=sim)",
        bn.query_poluicao(
            incendio="sim"
        )
    )

    print("\n" + "=" * 60)
    print("Fim da execução.")
    print("=" * 60)

    # Se quiseres ver todas as CPDs, descomenta esta linha:
    # bn.mostrar_cpds()


if __name__ == "__main__":
    ficheiro = sys.argv[1] if len(sys.argv) > 1 else "alert_results.csv"
    main(ficheiro)
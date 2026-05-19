import os
import re
import pandas as pd
from google import genai

from dotenv import load_dotenv
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

if not API_KEY:
    raise ValueError("Erro: coloca a GEMINI_API_KEY no ficheiro .env")

client = genai.Client(api_key=API_KEY)

def limpar_nome_ficheiro(texto):
    texto = texto.lower().strip()
    texto = re.sub(r"[^a-zA-Z0-9_]+", "_", texto)
    return texto


def obter_alertas(caminho_csv):
    df = pd.read_csv(caminho_csv)

    if "alertas" not in df.columns:
        raise ValueError("O ficheiro não tem a coluna 'alertas'.")

    alertas = (
        df["alertas"]
        .astype(str)
        .str.split(";")
        .explode()
        .str.strip()
        .unique()
    )

    alertas = [
        a for a in alertas
        if a and a.lower() not in ["sem_alerta", "sem alerta"]
    ]

    return sorted(alertas), df


def resumo_alerta(df, alerta):
    linhas_alerta = df[df["alertas"].astype(str).str.contains(alerta, na=False)]
    total = len(df)
    ocorrencias = len(linhas_alerta)
    percentagem = (ocorrencias / total) * 100 if total > 0 else 0

    return f"""
Alerta analisado: {alerta}
Total de registos no ficheiro: {total}
Número de ocorrências deste alerta: {ocorrencias}
Percentagem de ocorrência: {percentagem:.2f}%
"""


def criar_prompt(alerta, resumo):
    return f"""
Actua como um sistema de Inteligência Urbana para uma cidade sustentável.

Com base nos dados seguintes:

{resumo}

Gera um relatório em português de Portugal para o alerta "{alerta}".

IMPORTANTE:
- Não uses Markdown.
- Não uses símbolos como ##, ###, **, *, -, ``` ou tabelas Markdown.
- Escreve em texto limpo, próprio para ser colocado directamente num PDF.
- Usa títulos simples, por exemplo: "1. Resumo Executivo".
- Usa frases normais em parágrafos.

O relatório deve estar dividido exactamente nestas secções:

1. Resumo Executivo
Máximo 200 palavras. Explica o significado geral deste alerta.

2. Perspectiva do Cidadão
Linguagem simples. Explica como este alerta afecta o dia-a-dia. Dá conselhos práticos de segurança e saúde.

3. Perspectiva da Protecção Civil
Linguagem operacional. Explica que medidas podem ser tomadas no terreno. Refere riscos de falsos positivos e falsos negativos.

4. Perspectiva do Presidente da Câmara
Linguagem formal e estratégica. Dá 2 a 3 recomendações de acção para a cidade.

5. Perspectiva do Técnico de Dados Municipal
Linguagem analítica. Explica como os dados devem ser interpretados. Refere limitações dos dados.

6. Limitações e Riscos Éticos
Fala de transparência, enviesamentos, possíveis alucinações da IA e necessidade de validação humana.

Não inventes dados que não estejam no resumo.
"""


def gerar_texto_ia(prompt):
    resposta = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return resposta.text

def limpar_markdown(texto):
    texto = texto.replace("```", "")
    texto = texto.replace("###", "")
    texto = texto.replace("##", "")
    texto = texto.replace("#", "")
    texto = texto.replace("**", "")
    texto = texto.replace("__", "")
    texto = texto.replace("* ", "")
    texto = texto.replace("- ", "")
    texto = texto.replace("•", "")

    linhas_limpas = []

    for linha in texto.split("\n"):
        linha = linha.strip()

        if linha:
            linhas_limpas.append(linha)
        else:
            linhas_limpas.append("")

    return "\n".join(linhas_limpas)

def guardar_pdf(alerta, texto, pasta_saida="pdfs_alertas"):
    os.makedirs(pasta_saida, exist_ok=True)

    texto = limpar_markdown(texto)

    nome_pdf = limpar_nome_ficheiro(alerta) + ".pdf"
    caminho_pdf = os.path.join(pasta_saida, nome_pdf)

    doc = SimpleDocTemplate(
        caminho_pdf,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph(f"Relatório do Alerta: {alerta}", styles["Title"]))
    story.append(Spacer(1, 14))

    for linha in texto.split("\n"):
        linha = linha.strip()

        if not linha:
            story.append(Spacer(1, 8))

        elif linha.startswith("1. ") or linha.startswith("2. ") or linha.startswith("3. ") or linha.startswith("4. ") or linha.startswith("5. ") or linha.startswith("6. "):
            story.append(Spacer(1, 8))
            story.append(Paragraph(linha, styles["Heading2"]))
            story.append(Spacer(1, 6))

        else:
            story.append(Paragraph(linha, styles["BodyText"]))
            story.append(Spacer(1, 4))

    doc.build(story)

    return caminho_pdf


def main():
    caminho_alertas = "../Modulo_1/alert_results.csv"

    print("A ler alert_results.csv...")
    alertas, df = obter_alertas(caminho_alertas)

    print(f"Foram encontrados {len(alertas)} tipos de alerta:")
    for alerta in alertas:
        print(f"- {alerta}")

    for alerta in alertas:
        print(f"\nA gerar relatório para: {alerta}")

        resumo = resumo_alerta(df, alerta)
        prompt = criar_prompt(alerta, resumo)
        texto = gerar_texto_ia(prompt)
        caminho_pdf = guardar_pdf(alerta, texto)

        print(f"PDF criado: {caminho_pdf}")

    print("\nTodos os PDFs foram gerados com sucesso.")


if __name__ == "__main__":
    main()
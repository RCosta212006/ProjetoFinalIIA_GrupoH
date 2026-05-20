import os
import re
import pandas as pd
import time
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
        if a
        and a.lower() not in ["sem_alerta", "sem alerta", "nan"]
    ]

    return sorted(alertas), df

def resumo_alerta(df, alerta):
    linhas_alerta = df[df["alertas"].astype(str).str.contains(alerta, na=False)]
    total = len(df)
    ocorrencias = len(linhas_alerta)
    percentagem = (ocorrencias / total) * 100 if total > 0 else 0

    resumo = f"""
DADOS DO MÓDULO 1 — ALERTAS

Alerta analisado: {alerta}
Total de registos no ficheiro alert_results.csv: {total}
Número de ocorrências deste alerta: {ocorrencias}
Percentagem de ocorrência deste alerta: {percentagem:.2f}%
"""

    if "acoes_recomendadas" in df.columns and ocorrencias > 0:
        acoes = (
            linhas_alerta["acoes_recomendadas"]
            .astype(str)
            .str.split(";")
            .explode()
            .str.strip()
            .value_counts()
            .head(5)
        )

        resumo += "\nAcções recomendadas mais frequentes associadas a este alerta:\n"
        resumo += acoes.to_string()

    colunas_ambientais = [
        "temperature_c",
        "humidity_percent",
        "wind_speed_kmh",
        "precipitation_mm",
        "NO2",
        "PM10",
        "PM2.5",
        "O3"
    ]

    colunas_existentes = [c for c in colunas_ambientais if c in df.columns]

    if colunas_existentes and ocorrencias > 0:
        medias = linhas_alerta[colunas_existentes].mean(numeric_only=True)
        resumo += "\n\nValores médios das variáveis ambientais nos registos deste alerta:\n"

        for coluna, valor in medias.items():
            resumo += f"{coluna}: {valor:.2f}\n"

    try:
        df_metricas = pd.read_csv("../Modulo_2/metrics.csv")

        resumo += "\nDADOS DO MÓDULO 2 — MÉTRICAS DOS MODELOS\n"
        resumo += df_metricas.to_string(index=False)

    except FileNotFoundError:
        resumo += "\nDADOS DO MÓDULO 2 — MÉTRICAS DOS MODELOS\n"
        resumo += "O ficheiro metrics.csv não foi encontrado.\n"

    return resumo

def criar_prompt(alerta, resumo):
    return f"""
Actua como um Sistema de Inteligência Urbana para uma cidade sustentável.

Recebeste dados reais dos Módulos 1 e 2 do projecto:

{resumo}

O alerta em análise é: "{alerta}"

Gera um relatório em português de Portugal para ser convertido directamente num ficheiro PDF.

REGRAS IMPORTANTES DE FORMATAÇÃO:
Não uses Markdown.
Não uses símbolos como ##, ###, **, *, -, ``` ou tabelas Markdown.
Não uses listas com asteriscos.
Não uses blocos de código.
Escreve em texto limpo, com títulos simples e parágrafos normais.
Usa numeração simples apenas nos títulos das secções, por exemplo: "1. Resumo Executivo".
O texto deve estar pronto para aparecer num PDF formal.

REGRAS IMPORTANTES SOBRE OS DADOS:
Usa obrigatoriamente os valores disponíveis no resumo.
Refere o número de ocorrências do alerta.
Refere a percentagem de ocorrência do alerta.
Se existirem dados ambientais associados ao alerta, comenta-os.
Se existirem acções recomendadas no Módulo 1, menciona-as.
Se existirem métricas do Módulo 2, usa-as para comentar a fiabilidade dos modelos.
Não inventes valores, percentagens, métricas ou conclusões que não estejam nos dados.
Se algum dado estiver em falta, escreve claramente que esse dado não está disponível.

O relatório deve estar dividido exactamente nestas secções:

1. Resumo Executivo
Escreve no máximo 200 palavras.
Explica o significado geral do alerta "{alerta}".
Inclui o número de ocorrências e a percentagem de ocorrência.
Relaciona o alerta com a gestão urbana, segurança pública e qualidade de vida.

2. Dados Observados no Sistema
Apresenta uma explicação clara dos dados usados.
Refere:
número total de registos analisados;
número de ocorrências deste alerta;
percentagem de ocorrência;
principais acções recomendadas associadas ao alerta;
valores ambientais relevantes, se existirem no resumo.

3. Perspectiva do Cidadão
Usa linguagem simples, empática e directa.
Explica como este alerta pode afectar o dia-a-dia.
Dá recomendações práticas de saúde, segurança e prevenção.
Evita linguagem demasiado técnica.

4. Perspectiva da Protecção Civil
Usa linguagem operacional.
Explica como este alerta pode apoiar decisões no terreno.
Refere medidas de prevenção, resposta e priorização de meios.
Comenta os riscos de falsos positivos e falsos negativos.
Relaciona a resposta operacional com a frequência do alerta.

5. Perspectiva do Presidente da Câmara
Usa linguagem formal e estratégica.
Explica a importância deste alerta para a gestão da cidade.
Inclui 2 a 3 recomendações de acção para políticas públicas.
Relaciona o alerta com planeamento urbano, mobilidade, saúde pública ou comunicação com cidadãos.

6. Perspectiva do Técnico de Dados Municipal
Usa linguagem analítica.
Interpreta os dados do alerta.
Comenta a qualidade e limitações dos dados.
Usa as métricas do Módulo 2, quando disponíveis, para explicar a fiabilidade dos modelos.
Distingue claramente dados observados de previsões feitas por modelos.

7. Limitações e Riscos Éticos
Inclui uma análise crítica sobre:
transparência do sistema;
possíveis enviesamentos nos dados;
risco de alucinações da IA generativa;
risco de dependência excessiva de sistemas automáticos;
necessidade de validação humana antes de decisões reais.

8. Conclusão
Resume a importância do alerta "{alerta}".
Explica como a combinação dos Módulos 1, 2 e 3 pode apoiar uma cidade mais segura e sustentável.
"""

def gerar_texto_ia(prompt, tentativas=5, espera=30):
    for tentativa in range(1, tentativas + 1):
        try:
            resposta = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )
            return resposta.text

        except Exception as e:
            erro = str(e)

            if "503" in erro or "UNAVAILABLE" in erro or "high demand" in erro:
                print(f"Modelo indisponível. Tentativa {tentativa}/{tentativas}.")
                print(f"A aguardar {espera} segundos...")
                time.sleep(espera)
                continue

            if "429" in erro or "RESOURCE_EXHAUSTED" in erro or "quota" in erro.lower():
                print("Limite da API atingido.")
                print("Espera alguns minutos e volta a correr o script.")
                return None

            print(f"Erro inesperado ao chamar a IA: {e}")
            return None

    print("Não foi possível gerar texto após várias tentativas.")
    return None


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
        nome_pdf = limpar_nome_ficheiro(alerta) + ".pdf"
        caminho_pdf = os.path.join("pdfs_alertas", nome_pdf)

        if os.path.exists(caminho_pdf):
            print(f"PDF já existe, a ignorar: {caminho_pdf}")
            continue

        resumo = resumo_alerta(df, alerta)
        prompt = criar_prompt(alerta, resumo)
        texto = gerar_texto_ia(prompt)

        if texto is None:
            print(f"Não foi possível gerar relatório para '{alerta}'.")
            print("A continuar para o próximo alerta...")
            continue

        caminho_pdf = guardar_pdf(alerta, texto)
        print(f"PDF criado: {caminho_pdf}")

    print("\nTodos os PDFs foram gerados com sucesso.")

if __name__ == "__main__":
    main()
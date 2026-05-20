# Projeto Final de Introdução à Inteligência Artificial

## Descrição

Este projeto explora a aplicação de diferentes áreas da Inteligência Artificial no contexto de uma cidade sustentável.

O objectivo principal é apoiar decisões relacionadas com:

- Qualidade do ar;
- Mobilidade urbana;
- Alertas ambientais;
- Comunicação com cidadãos e decisores;
- Gestão de riscos urbanos.

O projeto está dividido em três módulos:

1. **Módulo 1 — Sistema Baseado em Conhecimento**
2. **Módulo 2 — Aprendizagem Automática**
3. **Módulo 3 — IA Generativa**

Cada módulo utiliza o ficheiro `processed_lisboa_porto_air_quality.csv` ou resultados derivados desse ficheiro.

---

## Estrutura do Projeto

```text
ProjetoFinalIIA_GrupoH
├── Modulo_1
│   ├── rules_engine.py
│   ├── bayes_alert.py
│   └── alert_results.csv
│
├── Modulo_2
│   ├── eda.ipynb
│   ├── train_classification.py
│   ├── train_regression.py
│   ├── metrics.csv
│   ├── melhor_modelo_classificacao.pkl
│   └── melhor_modelo_regressao.pkl
│
├── Modulo_3
│   ├── gen_report.py
│   ├── prompts_examples.md
│   ├── requirements.txt
│   ├── .env.example
│   │
│   ├── pdfs_alertas_prompt1
│   │   ├── frio_extremo.pdf
│   │   ├── humidade_baixa.pdf
│   │   ├── ozono_alto.pdf
│   │   ├── particulas_pm10_altas.pdf
│   │   ├── particulas_pm25_altas.pdf
│   │   ├── poluicao_no2_alta.pdf
│   │   ├── risco_calor_extremo.pdf
│   │   ├── risco_incendio_moderado.pdf
│   │   └── risco_nevoeiro.pdf
│   │
│   ├── pdfs_alertas_prompt2
│   │   ├── frio_extremo.pdf
│   │   ├── humidade_baixa.pdf
│   │   ├── ozono_alto.pdf
│   │   ├── particulas_pm10_altas.pdf
│   │   ├── particulas_pm25_altas.pdf
│   │   ├── poluicao_no2_alta.pdf
│   │   ├── risco_calor_extremo.pdf
│   │   ├── risco_incendio_moderado.pdf
│   │   └── risco_nevoeiro.pdf
│   │
│   └── pdfs_alertas_prompt3
│       ├── frio_extremo.pdf
│       ├── humidade_baixa.pdf
│       ├── ozono_alto.pdf
│       ├── particulas_pm10_altas.pdf
│       ├── particulas_pm25_altas.pdf
│       ├── poluicao_no2_alta.pdf
│       ├── risco_calor_extremo.pdf
│       ├── risco_incendio_moderado.pdf
│       └── risco_nevoeiro.pdf
│
├── processed_lisboa_porto_air_quality.csv
├── Gestao_de_Riscos_Ambientais.png
└── README.md
```

---

# Módulo 1 — Sistema Baseado em Conhecimento para Gestão de Emergências

## Objetivo

O Módulo 1 implementa um sistema de apoio à decisão para a Proteção Civil, capaz de analisar dados ambientais e gerar alertas.

Este módulo combina:

- Regras lógicas do tipo “if-else";
- Raciocínio simbólico;
- Criação de alertas;
- Rede bayesiana simples para lidar com incerteza.

---

## Ficheiros

```text
Modulo_1
├── rules_engine.py
├── bayes_alerts.py
└── alert_results.csv
```

---

## Motor de Regras

O ficheiro `rules_engine.py` lê o dataset original e aplica regras hardcoded dentro da função `sistema_de_regras()`.

As regras não estão num ficheiro JSON. Foram implementadas directamente no código com `if` e `elif`, conforme pedido pela professora.

Exemplo de regra:

```python
if temp >= 30 and humidade <= 35 and vento >= 20:
    alertas.append("risco_incendio_alto")
    acoes.append("Activar meios de vigilância e prevenção de incêndios")
```

O resultado é guardado no ficheiro:

```text
alert_results.csv
```

Este ficheiro contém os dados originais mais duas novas colunas:

- `alertas`
- `acoes_recomendadas`

---

## Tipos de Alertas

O sistema pode gerar alertas como:

- `frio_extremo`
- `humidade_baixa`
- `ozono_alto`
- `particulas_pm10_altas`
- `particulas_pm25_altas`
- `poluicao_no2_alta`
- `risco_calor_extremo`
- `risco_incendio_moderado`
- `risco_nevoeiro`

---

## Rede Bayesiana

O ficheiro `bayes_alerts.py` constrói uma rede bayesiana discreta com base nos dados do ficheiro `alert_results.csv`.

A rede não tem probabilidades hardcoded. As probabilidades são estimadas automaticamente a partir dos dados.

A estrutura usada é:

```text
temp ───────→ incendio
humidade ───→ incendio
vento ──────→ incendio

pm10 ───────→ poluicao
no2 ────────→ poluicao
o3 ─────────→ poluicao
incendio ───→ poluicao
```

Antes de treinar a rede, os dados são discretizados.

Exemplo:

```text
temperature_c = 28.4  →  temp = quente
humidity_percent = 25 →  humidade = baixa
```

A rede calcula probabilidades como:

```text
P(incendio | temp=quente)
P(incendio | temp=quente, humidade=baixa, vento=moderado)
P(poluicao | incendio=sim)
```

---

## Fontes das Regras do Módulo 1

As regras do Módulo 1 foram definidas como heurísticas simplificadas para contexto académico. Os limiares foram adaptados a partir de referências técnicas e ambientais, mas ajustados ao dataset usado no projeto para garantir que os alertas eram gerados de forma observável.

### Qualidade do Ar

Foram consideradas referências internacionais e europeias sobre poluentes atmosféricos, nomeadamente:

- PM10
- PM2.5
- NO2
- O3

Fontes consultadas:

```text
World Health Organization — WHO Global Air Quality Guidelines
https://www.who.int/publications/i/item/9789240034228

European Commission — EU Air Quality Standards
https://environment.ec.europa.eu/topics/air/air-quality/eu-air-quality-standards_en
```

Estas fontes serviram como base conceptual para regras relacionadas com:

```text
poluicao_no2_alta
particulas_pm10_altas
particulas_pm25_altas
ozono_alto
```

### Avisos Meteorológicos

Para regras relacionadas com precipitação, vento, frio, calor e nevoeiro, foram considerados critérios de avisos meteorológicos do IPMA.

Fonte consultada:

```text
IPMA — Critérios de Emissão dos Avisos Meteorológicos
https://www.ipma.pt/pt/enciclopedia/otempo/sam/index.html?page=criterios.xml
```

Esta fonte serviu como base conceptual para regras relacionadas com:

```text
frio_extremo
risco_calor_extremo
risco_nevoeiro
vento_forte
risco_inundacao
```

### Nota sobre os limiares

Os limiares finais usados no código não correspondem necessariamente aos valores oficiais exatos das entidades referidas. Foram ajustados para fins académicos, tendo em conta:

- a escala dos dados disponíveis;
- a necessidade de gerar alertas suficientes para análise;
- a demonstração do funcionamento do motor de regras;
- a integração posterior com a rede bayesiana.

---

## Como executar o Módulo 1

A partir da pasta principal:

```bash
python Modulo_1/rules_engine.py processed_lisboa_porto_air_quality.csv
```

Depois:

```bash
python Modulo_1/bayes_alerts.py Modulo_1/alert_results.csv
```

---

# Módulo 2 — Aprendizagem Automática para Mobilidade e Qualidade do Ar

## Objetivo

O Módulo 2 aplica modelos de aprendizagem automática supervisionada para prever:

1. Se a qualidade do ar é boa;
2. A concentração de NO2.

Este módulo distingue duas tarefas:

- **Classificação**;
- **Regressão**.

---

## Ficheiros

```text
Modulo_2
├── eda.ipynb
├── train_classification.py
├── train_regression.py
├── metrics.csv
└── models
```

---

## EDA — Análise Exploratória

O ficheiro `eda.ipynb` contém a análise exploratória dos dados.

Foram analisados:

- Estatísticas descritivas;
- Tipos de dados;
- Valores em falta;
- Histogramas;
- Correlações;
- Distribuição das variáveis;
- Possíveis relações entre poluentes e qualidade do ar.

---

## Classificação

A classificação tem como objetivo prever a variável:

```text
air_quality_good
```

Foram treinados dois modelos:

- Logistic Regression
- Random Forest Classifier

Foram usadas métricas como:

- Accuracy;
- Precision;
- Recall;
- F1-score;
- ROC AUC.

---

## Regressão

A regressão tem como objetivo prever a concentração de:

```text
NO2
```

Foram treinados modelos como:

- Linear Regression
- Random Forest Regressor

Foram usadas métricas como:

- MAE;
- RMSE;
- R2.

---

## Modelos Guardados

Os modelos treinados foram guardados em formato `.pkl`, permitindo reutilização sem necessidade de novo treino.

Exemplos:

```text
logistic_regression.pkl
random_forest_classifier.pkl
linear_regression_no2.pkl
random_forest_regressor_no2.pkl
```

---

## Métricas

As métricas dos modelos foram guardadas em:

```text
metrics.csv
```

Este ficheiro permite comparar os modelos e justificar a escolha do melhor modelo para cada tarefa.

---

## Como executar o Módulo 2

Classificação:

```bash
python Modulo_2/train_classification.py processed_lisboa_porto_air_quality.csv --output-dir Modulo_2
```

Regressão:

```bash
python Modulo_2/train_regression.py processed_lisboa_porto_air_quality.csv --output-dir Modulo_2
```

---

# Módulo 3 — IA Generativa para Relatórios por Tipo de Alerta

## Objetivo

O Módulo 3 utiliza uma API externa de IA Generativa para criar relatórios automáticos a partir dos alertas gerados no Módulo 1.

O sistema gera um PDF por cada tipo de alerta existente em `alert_results.csv`.

Cada PDF contém:

- resumo executivo;
- dados observados no sistema;
- perspectiva do cidadão;
- perspectiva da Protecção Civil;
- perspectiva do Presidente da Câmara;
- perspectiva do Técnico de Dados Municipal;
- limitações e riscos éticos;
- conclusão.

Além dos PDFs finais, foram testadas três variantes de prompt engineering. Os outputs dessas três experiências foram guardados na pasta `outputs_prompts`, e a análise encontra-se em `prompts_examples.md`.
---

## Ficheiros

```text
Modulo_3
├── gen_report.py
├── prompts_examples.md
├── requirements.txt
├── .env
├── pdfs_alertas_prompt1
│   ├── frio_extremo.pdf
│   ├── humidade_baixa.pdf
│   ├── ozono_alto.pdf
│   ├── particulas_pm10_altas.pdf
│   ├── particulas_pm25_altas.pdf
│   ├── poluicao_no2_alta.pdf
│   ├── risco_calor_extremo.pdf
│   ├── risco_incendio_moderado.pdf
│   └── risco_nevoeiro.pdf
├── pdfs_alertas_prompt2
│   └── exemplos de PDFs gerados com a segunda prompt
└── pdfs_alertas_prompt3
    └── exemplos de PDFs gerados com a terceira prompt
```

---

## Funcionamento

O ficheiro `gen_report.py`:

1. Lê o ficheiro `Modulo_1/alert_results.csv`;
2. Identifica todos os tipos de alerta;
3. Exclui `sem_alerta`, quando aplicável;
4. Cria um prompt para cada alerta;
5. Envia o prompt para uma API externa de IA;
6. Limpa símbolos de Markdown;
7. Cria um PDF final por alerta.

---

## Organização dos outputs

Os outputs das três variantes de prompt foram guardados em pastas separadas:

- `pdfs_alertas_prompt1`: contém os PDFs finais gerados com a prompt estruturada multi-perspectiva;
- `pdfs_alertas_prompt2`: contém os PDFs gerados com a prompt orientada para comunicação pública;
- `pdfs_alertas_prompt3`: contém os PDFs gerados com a prompt técnico-estratégica.

Esta organização permite comparar directamente como diferentes estratégias de prompt engineering alteram o tipo de relatório produzido pela IA generativa.

---

## Exemplo de PDFs Gerados

```text
pdfs_alertas/frio_extremo.pdf
pdfs_alertas/humidade_baixa.pdf
pdfs_alertas/ozono_alto.pdf
pdfs_alertas/particulas_pm10_altas.pdf
pdfs_alertas/risco_incendio_moderado.pdf
```

---

## API Externa

O Módulo 3 usa a API Gemini.

O ficheiro `.env` deve conter:

```env
GEMINI_API_KEY="coloca_a_tua_api_key"
GEMINI_MODEL="gemini-2.5-flash"
```

A API key não deve ser colocada diretamente no código nem enviada para o GitHub.

---

## Instalação das dependências

Dentro da pasta principal do projeto:

```bash
pip install -r Modulo_3/requirements.txt
```

O ficheiro `requirements.txt` deve conter:

```text
pandas
python-dotenv
google-genai
reportlab
```

---

## Como executar o Módulo 3

A partir da pasta `Modulo_3`:

```bash
python gen_report.py
```

Os PDFs serão criados em:

```text
Modulo_3/pdfs_alertas
```

---

## Prompt Engineering

O Módulo 3 testa diferentes perspectivas de comunicação a partir dos mesmos dados.

As perspetivas usadas são:

### 1. Cidadão

Objetivo:

- Linguagem simples;
- Explicação acessível;
- Recomendações práticas para saúde e segurança.

### 2. Proteção Civil

Objetivo:

- Linguagem operacional;
- Resposta no terreno;
- Riscos de falsos positivos e falsos negativos.

### 3. Presidente da Câmara

Objetivo:

- Linguagem formal;
- Visão estratégica;
- Recomendações de políticas públicas.

### 4. Técnico de Dados Municipal

Objetivo:

- Linguagem analítica;
- Interpretação dos dados;
- Limitações e fiabilidade.

Esta abordagem demonstra como a mesma informação pode ser comunicada de formas diferentes consoante o público-alvo.

---

## Limitações e Riscos Éticos

O projeto reconhece várias limitações:

- Os alertas dependem de regras simplificadas;
- Os modelos de machine learning dependem da qualidade dos dados;
- A IA generativa pode produzir erros ou alucinações;
- Os dados podem conter enviesamentos;
- As decisões automáticas devem ser validadas por humanos;
- Os resultados devem ser usados como apoio à decisão, não como substituição de especialistas.

---

# Como Executar o Projeto Completo

## 1. Módulo 1

```bash
python Modulo_1/rules_engine.py processed_lisboa_porto_air_quality.csv
python Modulo_1/bayes_alerts.py Modulo_1/alert_results.csv
```

## 2. Módulo 2

```bash
python Modulo_2/train_classification.py processed_lisboa_porto_air_quality.csv --output-dir Modulo_2
python Modulo_2/train_regression.py processed_lisboa_porto_air_quality.csv --output-dir Modulo_2
```

## 3. Módulo 3

```bash
cd Modulo_3
python gen_report.py
```

---

# Resultados Esperados

No final, o projeto produz:

- Alertas ambientais;
- Ações recomendadas;
- Probabilidades bayesianas;
- Modelos de classificação;
- Modelos de regressão;
- Métricas de desempenho;
- PDF's por tipo de alerta;
- Análise crítica e ética.

---

# Considerações Finais

Este projeto mostra como diferentes técnicas de Inteligência Artificial podem ser combinadas para apoiar uma cidade sustentável.

O Módulo 1 usa conhecimento simbólico e regras.

O Módulo 2 usa aprendizagem automática para previsão.

O Módulo 3 usa IA generativa para comunicar os resultados a diferentes públicos.

Apesar do potencial destas ferramentas, os resultados devem ser interpretados com cuidado e sempre acompanhados por validação humana.
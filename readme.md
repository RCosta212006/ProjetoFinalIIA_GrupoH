## Módulo 1 — Sistema Baseado em Conhecimento para Gestão de Emergências
📌 Descrição

Este módulo implementa um sistema de apoio à decisão para a Protecção Civil, capaz de:

Detectar riscos ambientais a partir de dados reais;
Gerar alertas e acções recomendadas com base em regras;
Modelar incerteza através de uma rede bayesiana simples.

O sistema combina IA simbólica (regras) com IA probabilística (rede bayesiana).

📂 Estrutura
.
├── rules_engine.py
├── bayes_alerts.py
├── alert_results.csv
├── processed_lisboa_porto_air_quality.csv
└── README.md
⚙️ Funcionamento
1. Motor de Regras

O ficheiro rules_engine.py:

Lê o dataset de entrada;
Aplica regras "se-então" (hardcoded com if/elif);
Gera alertas e acções recomendadas;
Guarda os resultados em alert_results.csv.

Exemplo de regra:

Se temperatura > 40°C ∧ humidade < 20% → risco_incendio_alto
2. Ficheiro intermédio

O ficheiro alert_results.csv contém:

Dados originais;
Coluna alertas;
Coluna acoes_recomendadas.

Este ficheiro serve como base para a rede bayesiana.

3. Rede Bayesiana

O ficheiro bayes_alerts.py:

Lê alert_results.csv;
Converte alertas em variáveis booleanas:
Incendio
Calor
Vento
Poluicao
Calcula probabilidades usando inferência por enumeração.
🧠 Metodologia
IA Simbólica (Regras)

As regras representam conhecimento explícito:

if temp > 40 and humidade < 20:
    risco_incendio_alto

Estas regras transformam dados numéricos em significado.

IA Probabilística (Rede Bayesiana)

A rede bayesiana calcula probabilidades com base na frequência dos dados:

P(Calor)
P(Incendio | Calor=True)
P(Poluicao | Calor=True)

Exemplo:

P(Incendio | Calor=True) = nº casos com incêndio e calor / nº casos com calor
▶️ Como executar
1. Gerar alertas
python rules_engine.py processed_lisboa_porto_air_quality.csv

Gera:

alert_results.csv
2. Executar rede bayesiana
python bayes_alerts.py alert_results.csv

Exemplo de output:

P(Calor): 0.40
P(Incendio | Calor=True): 0.50
⚠️ Decisões de implementação
As regras foram hardcoded conforme solicitado (sem regras.json);
A rede bayesiana não é hardcoded:
As probabilidades são calculadas automaticamente a partir dos dados;
Existe separação clara entre:
Sistema simbólico (regras)
Sistema probabilístico (inferência)


## Fontes para as regras:
- https://prociv.gov.pt
    - A Proteção Civil indica que temperaturas elevadas, baixa humidade e vento favorecem o risco e a propagação de incêndios.
- https://www.eea.europa.eu
    - A EEA identifica ondas de calor como eventos extremos com impacto significativo na saúde pública e no ambiente urbano.
- https://wmo.int
    - A WMO define ondas de calor como períodos prolongados de temperatura anormalmente elevada, podendo justificar alertas baseados em limiares térmicos.
- https://www.ipma.pt
    - O IPMA utiliza limiares de precipitação e vento para emitir avisos meteorológicos, justificando a utilização de regras baseadas nestas variáveis.
- https://www.who.int
    - A OMS estabelece valores de referência para partículas finas (PM2.5), sendo níveis acima de 25 µg/m³ considerados prejudiciais à saúde a curto prazo.
- https://www.epa.gov
    - A EPA identifica hidrocarbonetos não metânicos (NMHC) como precursores da formação de ozono troposférico, justificando a sua inclusão em regras de qualidade do ar.


Regras baseadas em incêndio, calor e propagação

Regra -> fire_high:
- A ANEPC/DECIR considera temperatura, humidade relativa e vento como factores relevantes no risco de incêndio rural.
- Esta regra foi definida com base na relevância operacional da temperatura e da humidade relativa na avaliação do risco de incêndio rural, referida na documentação da Protecção Civil.

Regra -> fire_spread:
- A documentação da Protecção Civil e DECIR reforça a importância de vento, temperatura e humidade na perigosidade e propagação do incêndio rural.

Regra -> extreme_heat:
- O IPMA emite avisos para “tempo quente”, e a WMO enquadra as ondas de calor como fenómenos meteorológicos extremos que justificam alertas.
- O IPMA usa avisos para tempo quente e a WMO reconhece ondas de calor como fenómenos extremos.

Regras baseadas em precipitação e vento

Regra -> heavy_rain:
- O IPMA usa 10–20 mm/1h como intervalo de aviso amarelo para precipitação.


Por indicação da docente, a base de conhecimentos foi implementada directamente no ficheiro rules_engine.py, através da função load_rules(), em vez de ser guardada num ficheiro regras.json.
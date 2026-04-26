# Informações :)
O sistema foi dividido em dois componentes principais.
O primeiro (rules_engine.py) implementa um sistema baseado em conhecimento com regras “se-então”, responsável pela inferência determinística de riscos e acções.
O segundo (bayes_alerts.py) implementa uma Rede Bayesiana simples para modelar incerteza e actualizar probabilidades com base em evidência observada.

O sistema desenvolvido integra diferentes tipos de risco — meteorológicos, ambientais e de qualidade do ar — permitindo uma abordagem híbrida à avaliação de alertas. 
Para além de regras específicas para cada fenómeno, foram incluídas regras combinadas que capturam interacções entre variáveis, como calor extremo e poluição, ou vento forte e risco de incêndio, aproximando o sistema de cenários reais mais complexos.

A Rede Bayesiana complementa o motor de regras. Enquanto as regras do rules_engine.py produzem conclusões determinísticas, a Rede Bayesiana permite representar incerteza. Neste exemplo, os nós HeatExtreme, LowHumidity e StrongWind influenciam probabilisticamente o nó FireRisk. Assim, em vez de concluir apenas que existe ou não risco, o sistema estima a probabilidade de risco de incêndio com base na evidência observada.

Estrutura das regras

Cada regra tem:
- condição
- risco
- prioridade
- ação

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

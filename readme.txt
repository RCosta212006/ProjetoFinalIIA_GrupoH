O sistema foi dividido em dois componentes principais.
O primeiro (rules_engine.py) implementa um sistema baseado em conhecimento com regras “se-então”, responsável pela inferência determinística de riscos e acções.
O segundo (bayes_alerts.py) implementa uma Rede Bayesiana simples para modelar incerteza e actualizar probabilidades com base em evidência observada.

O sistema desenvolvido integra diferentes tipos de risco — meteorológicos, ambientais e de qualidade do ar — permitindo uma abordagem híbrida à avaliação de alertas. 
Para além de regras específicas para cada fenómeno, foram incluídas regras combinadas que capturam interacções entre variáveis, como calor extremo e poluição, ou vento forte e risco de incêndio, aproximando o sistema de cenários reais mais complexos.

Estrutura das regras

Cada regra tem:
- condição
- risco
- prioridade
- ação
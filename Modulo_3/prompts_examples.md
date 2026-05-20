# Módulo 3 — Exemplos de Prompts e Análise dos Outputs

## Objectivo

Este ficheiro documenta três variantes de prompt engineering testadas no Módulo 3. O objectivo foi observar como a alteração da formulação do pedido à IA generativa influencia o tom, a estrutura, o detalhe técnico e a utilidade dos relatórios gerados em PDF.

Os relatórios foram gerados a partir dos dados do `alert_results.csv` e das métricas do `metrics.csv`, criando um PDF por tipo de alerta. Cada PDF inclui várias perspectivas: Cidadão, Protecção Civil, Presidente da Câmara, Técnico de Dados Municipal e Limitações e Riscos Éticos.

---

# Prompt 1 — Prompt Estruturado Multi-perspectiva

## Técnica usada

Structured prompting e audience prompting.

Esta variante obriga a IA a seguir uma estrutura fixa e a adaptar o conteúdo a diferentes públicos-alvo.

## Prompt

```text
Actua como um Sistema de Inteligência Urbana para uma cidade sustentável.

Recebeste dados reais dos Módulos 1 e 2 do projecto:

{resumo}

O alerta em análise é: "{alerta}"

Gera um relatório em português de Portugal para ser convertido directamente num ficheiro PDF.

REGRAS IMPORTANTES DE FORMATAÇÃO:
Não uses Markdown.
Não uses símbolos como ##, ###, negrito com asteriscos, listas com asteriscos, hífens, blocos de código ou tabelas Markdown.
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
```

## Output (Exemplo: Alerta de Frio Extremo)

### **1. Resumo Executivo**

O alerta de frio extremo é um indicador crítico para a gestão de uma cidade sustentável, servindo como gatilho
para medidas de proteção social e operacional. O sistema identificou 1176 ocorrências deste fenómeno,
representando uma incidência de 10,92 por cento nos registos analisados. Este alerta é essencial para a
manutenção da segurança pública e da qualidade de vida, permitindo que a administração municipal antecipe o
impacto das baixas temperaturas nos grupos de risco, bem como na fluidez da mobilidade urbana. A gestão
eficaz destes eventos reduz a pressão sobre os serviços de emergência e garante a proteção da população,
consolidando a resiliência da cidade perante condições climáticas adversas.

### **2. Dados Observados no Sistema**

O presente relatório baseia-se num universo de 10768 registos processados pelo sistema. O alerta de frio
extremo manifestou-se em 1176 dessas ocorrências. Relativamente às condições ambientais detetadas durante
estes episódios, verificou-se uma temperatura média de 5,16 graus Celsius e uma humidade relativa de 57,90 por
cento. Dados referentes a velocidade do vento, precipitação, PM10, PM2.5 e ozono não estão disponíveis. Como
principais medidas de resposta, o sistema recomenda a ativação imediata de apoio à população vulnerável, a
redução de tráfego em zonas críticas e a monitorização de risco de secura ambiental.

### **3. Perspectiva do Cidadão**

O frio extremo traz desafios claros para o nosso quotidiano, afetando principalmente a nossa saúde e conforto.
Nestes dias, é fundamental que proteja as extremidades do corpo, use várias camadas de roupa e mantenha a
sua habitação aquecida de forma segura. Evite esforços físicos intensos ao ar livre e procure verificar se os seus
vizinhos mais idosos ou em situação de isolamento precisam de auxílio. A circulação na cidade pode ser mais
difícil devido à gestão de tráfego, por isso, procure planear as suas deslocações com antecedência e utilize
transportes públicos sempre que possível. A sua prudência é a melhor forma de evitar doenças respiratórias e
acidentes causados pelo gelo ou humidade.

### **4. Perspetiva da Protecção Civil**

Operacionalmente, o alerta de frio extremo permite uma gestão proativa dos recursos de emergência. A
priorização recai sobre o apoio direto a populações em situação de sem-abrigo e isolamento, articulando com
equipas de intervenção social. A redução de tráfego em zonas críticas visa prevenir acidentes rodoviários e
garantir que as vias permaneçam desimpedidas para veículos prioritários. A eficácia deste sistema depende da
precisão dos modelos de classificação; uma elevada taxa de sucesso na identificação reduz o risco de falsos
positivos que poderiam esgotar meios desnecessariamente, bem como o risco de falsos negativos que deixariam
a população desprotegida.


### **5. Perspetiva do Presidente da Câmara**

A gestão urbana sustentável exige uma resposta rigorosa face a fenómenos de frio extremo. A proteção dos
cidadãos é a nossa prioridade absoluta. Recomendo três eixos de atuação: primeiro, o reforço dos centros de
acolhimento noturno e das equipas de rua para apoio social; segundo, o ajuste estratégico dos planos de
mobilidade, priorizando a segurança nos eixos rodoviários principais; e terceiro, a implementação de uma
comunicação institucional clara e contínua para informar os munícipes sobre as medidas de autoproteção. A
integração de tecnologia de monitorização permite uma governação baseada em evidências, garantindo que os
recursos públicos são alocados de forma eficiente onde o risco é mais elevado.

### **6. Perspetiva do Técnico de Dados Municipal**

A análise dos dados do Módulo 1 demonstra uma consistência nas variáveis de temperatura e humidade. No que
respeita à fiabilidade dos modelos do Módulo 2, observamos que o Random Forest Classifier apresenta uma
precisão notável, com uma exatidão de 0,98 e uma pontuação F1 de 0,97, superando a Regressão Logística.
Relativamente à regressão de níveis de NO2, os modelos apresentam um coeficiente de determinação R2 entre
0,70 e 0,71, o que indica uma capacidade preditiva moderadamente satisfatória. É imperativo distinguir que estes
modelos fornecem estimativas e probabilidades. A ausência de dados sobre PM10, PM2.5 e ozono limita a visão
holística da qualidade do ar nestes episódios, sendo uma lacuna que requer atenção técnica futura para
aumentar a robustez da análise.

### **7. Limitações e Riscos Éticos**

A utilização de sistemas automatizados implica responsabilidades significativas. Devemos assegurar total
transparência nos algoritmos utilizados para que a tomada de decisão seja explicável. Existe sempre o risco de
enviesamentos nos dados históricos, que podem refletir desigualdades na cobertura de sensores. Além disso, a
IA generativa não substitui o julgamento humano, existindo o risco de alucinações ou interpretações incorretas
dos dados. A dependência excessiva destas ferramentas pode levar a uma perda de competências analíticas
humanas. Por conseguinte, todas as decisões estratégicas baseadas nestes relatórios devem passar por uma
validação humana final antes da sua implementação operacional.

### **8. Conclusão**

O alerta de frio extremo constitui um pilar fundamental para a segurança e resiliência da nossa cidade. A
integração dos dados do Módulo 1, as métricas de performance do Módulo 2 e o apoio do Módulo 3 permite que
a administração municipal atue de forma rápida e precisa. Este ecossistema de inteligência urbana, embora
dependente de uma vigilância humana constante e crítica, oferece as ferramentas necessárias para construir um
ambiente mais seguro, sustentável e atento às necessidades reais de todos os cidadãos perante a instabilidade
climática.

---

### Objetivo da Prompt 1

O principal objetivo da Prompt 1 foi gerar um relatório geral a partir dos dados dos Módulos 1 e 2.

A prompt pediu à IA para transformar os resultados do sistema de alertas e dos modelos de machine learning num relatório compreensível, incluindo:

- resumo executivo;
- recomendações de acção;
- limitações;
- riscos éticos;
- interpretação dos resultados.

Esta prompt procurou avaliar se a IA conseguia organizar a informação de forma clara, seguindo uma estrutura fixa e adaptando o conteúdo a diferentes perspectivas institucionais e sociais.

---

## Análise do output

Esta foi a variante mais adequada para a entrega final, porque produziu relatórios completos e consistentes. A estrutura fixa garantiu que todos os PDFs tivessem as mesmas secções, facilitando a comparação entre alertas.

Os outputs passaram a incluir dados concretos, como número de ocorrências, percentagem de ocorrência, acções recomendadas e métricas dos modelos. Por exemplo, o relatório de `humidade_baixa` indica 2217 ocorrências, correspondendo a 20,59% dos registos analisados. O relatório de `poluicao_no2_alta` indica 5702 ocorrências, representando 52,95% dos registos, mostrando que este é o alerta mais frequente e estruturalmente mais relevante.

Esta prompt também ajudou a reduzir respostas vagas, porque obrigou a IA a usar os valores fornecidos no resumo e a não inventar métricas. A principal limitação observada foi que, apesar da instrução para não usar Markdown, a IA ainda pode ocasionalmente gerar símbolos ou formatação próxima de Markdown, sendo por isso necessária a função de limpeza antes da criação do PDF.

---

### Pontos fortes da Prompt 1

A principal vantagem da Prompt 1 foi a simplicidade. Como a instrução era direta, a IA conseguiu gerar rapidamente um relatório claro e organizado.

Outro ponto positivo foi a capacidade de sintetizar os resultados dos Módulos 1 e 2 sem tornar o texto demasiado complexo. Isto torna a prompt útil para obter uma primeira versão do relatório ou uma visão geral dos dados.

A Prompt 1 também mostrou que, mesmo sem exemplos ou papéis definidos, a IA consegue produzir uma resposta coerente quando recebe instruções claras sobre a estrutura pretendida.

---

### Limitações da Prompt 1

A principal limitação da Prompt 1 é que o output tende a ser mais genérico. Como não existe uma perspectiva específica nem uma técnica de adaptação ao público, a IA pode produzir uma resposta menos personalizada.

Outra limitação é que, se a prompt não obrigar explicitamente a usar valores concretos dos ficheiros `alert_results.csv` e `metrics.csv`, a IA pode focar-se mais em explicações gerais do que em dados quantitativos.

Também existe o risco de a resposta não distinguir claramente entre dados observados e previsões dos modelos. Por isso, esta prompt exige uma revisão humana para confirmar se as métricas e conclusões estão alinhadas com os dados reais.

---

### Conclusão da análise da Prompt 1

A Prompt 1 foi eficaz para produzir uma resposta geral e estruturada sobre os resultados do projecto. A sua simplicidade facilitou a geração rápida de um relatório inicial.

No entanto, por seguir uma estrutura bastante rígida, o output pode tornar-se menos flexível e menos criativo. A adaptação aos públicos existe, mas é feita dentro de um formato muito controlado.

Esta prompt demonstra bem a utilidade do zero-shot prompting, mas também mostra as suas limitações. Para a entrega final, esta prompt foi a mais adequada, porque combina estrutura fixa, várias perspectivas, dados quantitativos e uma secção crítica sobre limitações e riscos éticos.

---

# Prompt 2 — Prompt Orientado para Comunicação Pública

## Técnica usada

Audience prompting e role prompting.

Esta variante dá prioridade à clareza comunicacional, simulando que a IA escreve para a população e para entidades municipais que têm de comunicar riscos ambientais.

## Prompt

```text
Actua como um gabinete municipal de comunicação de risco ambiental.

Recebeste os seguintes dados dos Módulos 1 e 2:

{resumo}

O alerta em análise é: "{alerta}".

Gera um relatório em português de Portugal para ser colocado num PDF oficial da Câmara Municipal.

O texto deve ser claro, directo e compreensível para pessoas sem formação técnica.
Não uses Markdown, asteriscos, títulos com cardinal ou tabelas.
Não inventes dados que não estejam no resumo.

Organiza o relatório nas seguintes secções:

1. Resumo Executivo
Explica em menos de 200 palavras o que significa o alerta e porque é importante para a cidade.

2. O que os dados mostram
Indica o número total de registos, o número de ocorrências do alerta e a percentagem de ocorrência.
Explica as principais acções recomendadas e os valores ambientais mais relevantes.

3. Informação para o Cidadão
Explica como este alerta pode afectar a saúde, deslocações, rotina diária e segurança familiar.
Dá conselhos simples e práticos.

4. Informação para Serviços Municipais e Protecção Civil
Explica que medidas devem ser tomadas no terreno e como priorizar recursos.
Refere riscos de falsos positivos e falsos negativos.

5. Informação para Decisores Políticos
Apresenta 2 a 3 recomendações de acção para melhorar a resposta da cidade.

6. Limitações e Riscos Éticos
Explica a necessidade de transparência, validação humana, cuidado com enviesamentos e risco de alucinações da IA.

7. Conclusão
Resume a importância do alerta e da utilização responsável de IA.
```

## Output (Exemplo: Alerta de Frio Extremo)

### **1. Resumo Executivo**

Este relatório detalha o alerta de frio extremo detetado pelo nosso sistema de monitorização. O alerta é emitido
quando as condições meteorológicas atingem valores de temperatura que representam um risco para o
bem-estar da população, especialmente os grupos mais vulneráveis. A importância de monitorizar este fenómeno
reside na necessidade de prevenir problemas de saúde pública, reduzir incidentes rodoviários e assegurar o
apoio necessário às famílias em situação de carência. A nossa estratégia baseia-se na utilização de modelos de
inteligência artificial de alta precisão para antecipar estas condições, permitindo uma resposta célere e eficiente
por parte dos serviços municipais, salvaguardando assim a segurança e a qualidade de vida no nosso município.

### **2. O que os dados mostram**

O nosso sistema analisou um total de 10.768 registos ambientais. Destes, foram identificadas 1.176 ocorrências
de frio extremo, o que corresponde a uma frequência de 10,92 por cento. Durante estes episódios, a temperatura
média registada foi de 5,16 graus Celsius, com uma humidade média de 57,90 por cento. Observámos também
níveis elevados de dióxido de azoto, com uma média de 136,06, sugerindo que o frio extremo está
frequentemente associado a uma menor qualidade do ar. As ações mais frequentemente recomendadas pelo
sistema incluem a ativação imediata de apoio à população vulnerável, a redução do tráfego em zonas críticas e a
monitorização constante da secura ambiental.

### **3. Informação para o Cidadão**

O frio extremo pode afetar a saúde, aumentando o risco de doenças respiratórias e cardiovasculares.
Recomendamos que evite a exposição prolongada ao exterior e que mantenha a casa aquecida, garantindo
sempre a ventilação adequada se utilizar aquecedores a combustível. Nas deslocações, tenha cautela
redobrada, pois o frio pode tornar as vias escorregadias ou dificultar a condução. Proteja-se com várias camadas
de roupa e assegure-se de que os membros da família mais idosos ou dependentes estão confortáveis e bem
alimentados. Se detetar alguém em situação de isolamento ou sem abrigo, contacte os serviços municipais de
apoio social.

### **4. Informação para Serviços Municipais e Protecção Civil**

A Proteção Civil deve priorizar a ativação de equipas de apoio social e de rua para os grupos de risco. A gestão
de tráfego deve ser restringida em áreas onde a visibilidade ou a aderência ao solo estejam comprometidas. É
fundamental reconhecer que qualquer sistema de previsão pode falhar. Os falsos positivos podem levar ao
desperdício de recursos municipais, enquanto os falsos negativos podem resultar em falta de assistência. A
validação das recomendações por técnicos no terreno é essencial para garantir que os meios são aplicados onde
são efetivamente necessários.

### **5. Informação para Decisores Políticos**

Para melhorar a resposta da cidade, recomendamos, em primeiro lugar, o reforço da rede de centros de
acolhimento temporário durante o inverno. Em segundo lugar, propomos a implementação de um sistema de
sensores de qualidade do ar mais denso, dado que os dados revelam uma correlação preocupante entre o frio e
a acumulação de poluentes atmosféricos. Por fim, sugerimos a criação de um plano de comunicação direta com
os munícipes vulneráveis através de alertas por mensagem de texto, garantindo que as recomendações
cheguem atempadamente a quem mais precisa.

### **6. Limitações e Riscos Éticos**

A utilização de tecnologia de inteligência artificial exige rigor e transparência. Embora os nossos modelos de
classificação apresentem um desempenho elevado, é imperativo que os dados sejam sempre validados por
especialistas humanos. Existe o risco de erros de interpretação ou de enviesamentos nos dados históricos que
podem condicionar as decisões. Devemos ser cautelosos perante eventuais alucinações da tecnologia, que
podem gerar conclusões logicamente plausíveis, mas factualmente incorretas. A responsabilidade final pela
segurança pública cabe aos decisores municipais, utilizando a IA apenas como uma ferramenta de apoio e não
como um substituto do julgamento crítico.

### **7. Conclusão**

A gestão do risco ambiental exige uma combinação entre tecnologia avançada e supervisão humana diligente. O
alerta de frio extremo é um componente fundamental do nosso compromisso com a proteção da comunidade. Ao
utilizar estas ferramentas de forma responsável, estamos a garantir um município mais preparado, resiliente e
atento às necessidades dos seus cidadãos, mesmo perante condições meteorológicas adversas. A colaboração
entre os serviços municipais e a transparência para com a população continuarão a ser os pilares da nossa
estratégia de proteção ambiental.

---


### Objectivo da Prompt 2

O principal objectivo desta prompt foi testar se a IA conseguia adaptar a linguagem, o foco e o nível técnico da resposta consoante o destinatário.

A mesma informação sobre alertas ambientais e métricas dos modelos foi reorganizada em várias perspectivas:

- para o cidadão, com linguagem simples e conselhos práticos;
- para a Protecção Civil, com foco operacional;
- para o Presidente da Câmara, com foco estratégico e político;
- para o Técnico de Dados Municipal, com análise mais técnica dos modelos e limitações.

---

## Análise do output

Esta prompt gerou respostas mais acessíveis e orientadas para comunicação pública. A seção do cidadão tornou-se mais clara, com recomendações práticas como evitar esforço físico ao ar livre, proteger grupos vulneráveis e acompanhar avisos municipais.

Nos alertas ligados à qualidade do ar, como `ozono_alto`, `particulas_pm10_altas`, `particulas_pm25_altas` e `poluicao_no2_alta`, a IA explicou de forma compreensível os efeitos na saúde respiratória. No relatório de `ozono_alto`, por exemplo, o texto identifica o ozono troposférico como poluente que pode irritar pulmões e olhos, recomendando evitar exercício intenso ao ar livre em períodos críticos.

A vantagem desta variante é a facilidade de leitura. A desvantagem é que o relatório tende a ser menos técnico, usando as métricas do Módulo 2 de forma mais resumida. Assim, esta prompt seria melhor para um relatório de divulgação pública, mas menos completa para demonstrar a componente técnica do projecto.

---

### Pontos fortes da Prompt 2

A principal vantagem da Prompt 2 foi a sua capacidade de adaptar a comunicação. Esta abordagem tornou os relatórios mais úteis para diferentes públicos, mostrando que a IA generativa pode ser usada não só para resumir dados, mas também para ajustar o discurso conforme o contexto.

Outro ponto positivo foi a clareza das recomendações. A resposta para o cidadão ficou mais acessível, enquanto a resposta para entidades técnicas manteve maior detalhe operacional e analítico.

A prompt também ajudou a demonstrar que a engenharia de prompts influencia directamente o resultado. A IA não respondeu apenas com um relatório genérico; produziu conteúdos diferenciados consoante a função de cada interveniente na cidade.

---

### Limitações da Prompt 2

Apesar das vantagens, a Prompt 2 pode gerar respostas menos uniformes do que uma prompt mais estruturada. Como o foco principal está na adaptação da linguagem, existe o risco de a IA dar menos atenção à comparação sistemática dos dados entre alertas.

Outra limitação é que, se a prompt não obrigar explicitamente a usar valores concretos do `alert_results.csv` e do `metrics.csv`, a IA pode produzir uma resposta mais genérica. Por isso, é importante incluir no prompt instruções como: "usa obrigatoriamente o número de ocorrências, percentagem de ocorrência e métricas dos modelos".

Além disso, como esta prompt incentiva uma resposta mais interpretativa, existe maior risco de a IA extrapolar conclusões que não estão directamente nos dados. Isto reforça a necessidade de validação humana.

---

### Conclusão da análise da Prompt 2

A Prompt 2 foi eficaz para demonstrar técnicas de prompt engineering baseadas em papéis e públicos-alvo. O output gerado foi mais adaptado, comunicacional e contextualizado.

Esta prompt mostrou que a IA generativa consegue transformar dados técnicos em mensagens adequadas a diferentes necessidades urbanas. No entanto, para garantir rigor, a prompt deve ser acompanhada de instruções claras para usar dados concretos e evitar conclusões não suportadas.

Em suma, a Prompt 2 é uma boa opção para demonstrar criatividade e adaptação da IA, mas a prompt original continua a ser mais adequada para a geração final dos PDFs, por ser mais estruturada, completa e comparável entre os diferentes tipos de alerta.

# Prompt 3 — Prompt Técnico e Estratégico

## Técnica usada

Role prompting, data-grounded prompting e structured prompting.

Esta variante obriga a IA a assumir um papel mais técnico, valorizando a interpretação dos dados, as métricas de machine learning e as limitações do sistema.

## Prompt

```text
Actua como um Técnico de Dados Municipal responsável por apoiar decisões da Protecção Civil e da Câmara Municipal.

Foram-te fornecidos dados reais do sistema:

{resumo}

O alerta em análise é: "{alerta}".

Gera um relatório técnico em português de Portugal, pronto para PDF, sem Markdown e sem símbolos de formatação.

O relatório deve ser rigoroso e baseado apenas nos dados disponíveis.
Não inventes valores.
Sempre que uma variável ou métrica não estiver disponível, escreve que não está disponível.
Distingue dados observados, regras do Módulo 1 e previsões ou métricas do Módulo 2.

Divide o relatório nas seguintes secções:

1. Resumo Executivo
Resume o alerta, a sua frequência e a sua relevância operacional.

2. Análise Quantitativa do Alerta
Inclui número de ocorrências, percentagem de ocorrência, acções recomendadas e médias ambientais.
Interpreta a importância desses valores.

3. Interpretação Operacional para Protecção Civil
Explica como o alerta pode influenciar decisões no terreno, priorização de meios e comunicação de risco.
Inclui falsos positivos e falsos negativos.

4. Interpretação Estratégica para a Câmara Municipal
Apresenta 2 a 3 recomendações de política pública ou planeamento urbano.

5. Avaliação dos Modelos do Módulo 2
Comenta as métricas de classificação e regressão.
Indica qual modelo parece mais fiável para classificação e qual apresenta melhor desempenho para regressão.
Explica os limites de usar estas métricas para decisões reais.

6. Limitações, Riscos Éticos e Validação Humana
Analisa transparência, enviesamentos, alucinações da IA e dependência excessiva de automação.

7. Conclusão
Explica como a integração dos três módulos apoia uma cidade sustentável.
```

## Output (Exemplo: Alerta de Frio Extremo)

### **1. RESUMO EXECUTIVO**

O presente relatório analisa o alerta de frio extremo, identificado no sistema como um evento relevante para a
gestão municipal e proteção civil. Com 1176 ocorrências num universo de 10768 registos, este alerta representa
10,92% da amostra total. A sua relevância operacional é elevada, exigindo protocolos de atuação imediata,
nomeadamente na salvaguarda da população vulnerável e na gestão da mobilidade urbana.

### **2. ANÁLISE QUANTITATIVA DO ALERTA**

O alerta de frio extremo regista-se em 1176 situações, correspondendo a uma prevalência de 10,92%. As ações
recomendadas são: Ativar apoio a população vulnerável (1176 registos), Reduzir tráfego em zonas críticas (911
registos) e Monitorizar risco de secura ambiental (49 registos).

As variáveis ambientais apresentam os seguintes valores médios: temperatura de 5,16 graus Celsius e humidade
de 57,90%. O nível de NO2 regista uma média de 136,06. Os valores de velocidade do vento, precipitação,
PM10, PM2.5 e O3 não estão disponíveis nos registos. A elevada média de NO2 sugere uma correlação entre
períodos de frio extremo e a qualidade do ar, que deve ser monitorizada.

### **3. INTERPRETAÇÃO OPERACIONAL PARA PROTECÇÃO CIVIL**

Este alerta impõe a ativação imediata de equipas de apoio social para as populações em risco, dado que a
totalidade das ocorrências sinaliza esta necessidade. A recomendação de redução de tráfego deve ser articulada
com as forças de segurança para evitar congestionamentos em zonas críticas, que, sob temperaturas baixas,
podem dificultar manobras de emergência. A gestão de falsos positivos (alertas ativados sem risco real) é crucial
para evitar a exaustão de recursos; inversamente, os falsos negativos representam um risco direto para a
segurança da população, sendo necessário validar a sensibilidade do sistema para evitar a omissão de situações
de perigo real.

### **4. INTERPRETAÇÃO ESTRATÉGICA PARA A CÂMARA MUNICIPAL**

Primeiro, recomenda-se a criação de um plano de contingência habitacional focado na eficiência térmica para
edifícios em zonas onde o alerta é frequente. Segundo, sugere-se a implementação de um sistema de
sinalização variável no tráfego que responda automaticamente aos limiares de temperatura detetados, reduzindo
o fluxo em zonas específicas durante episódios de frio intenso. Terceiro, o investimento na ampliação da rede de
monitorização atmosférica, colmatando a ausência de dados de partículas finas (PM10 e PM2.5), é fundamental
para uma gestão de saúde pública mais rigorosa.

### **5. AVALIAÇÃO DOS MODELOS DO MÓDULO 2**

Na tarefa de classificação, o modelo Random Forest Classifier apresenta o melhor desempenho, com uma
Accuracy de 0,98 e um F1-Score de 0,97, superando a Regressão Logística. Na tarefa de regressão para
previsão de NO2, o modelo de Regressão Linear apresenta um R2 de 0,716, superior ao Random Forest
Regressor (0,700), sendo, por isso, o modelo de regressão mais fiável. Contudo, a utilização destas métricas
para decisões reais possui limites severos: a performance estatística não garante a infalibilidade do modelo em
condições meteorológicas atípicas ou em cenários de dados em falta.

### **6. LIMITAÇÕES, RISCOS ÉTICOS E VALIDAÇÃO HUMANA**

A transparência é condicionada pela ausência de dados em variáveis críticas. Existe o risco de enviesamento se
o modelo priorizar apenas as zonas onde existem sensores ativos. A dependência excessiva de automação pode
levar a alucinações algorítmicas, onde o sistema interpreta padrões de dados incompletos como factos. É
imperativo que qualquer decisão de intervenção no terreno tenha sempre a validação humana final, integrando o
conhecimento contextual que a máquina não possui.

### **7. CONCLUSÃO**

A integração dos dados de alerta, métricas de modelos e recomendações operacionais permite uma gestão
municipal mais proativa. A utilização destes módulos apoia a criação de uma cidade sustentável ao permitir uma
alocação eficiente de recursos, a mitigação de riscos de saúde pública e a otimização da circulação urbana,
garantindo que as políticas de proteção civil são sustentadas por evidência quantitativa rigorosa.

---

### Objectivo da Prompt 3

O principal objetivo da Prompt 3 foi testar se a IA conseguia gerar um relatório mais controlado e padronizado.

Ao contrário de uma prompt mais livre, esta abordagem obriga a IA a seguir uma sequência lógica de secções. Isto ajuda a garantir que todos os pontos importantes são incluídos:

- resumo executivo;
- dados quantitativos do alerta;
- interpretação para diferentes públicos;
- recomendações de acção;
- análise das métricas dos modelos;
- limitações e riscos éticos;
- conclusão.

Assim, a Prompt 3 foi pensada para produzir um output mais próximo do formato final exigido para os PDFs do Módulo 3.

---

## Análise do output

Esta prompt produziu relatórios mais técnicos e mais adequados à avaliação académica. A secção do Técnico de Dados Municipal ficou mais forte, porque passou a incluir a comparação dos modelos do Módulo 2.

Nos PDFs gerados, a IA identificou correctamente que o `Random Forest Classifier` obteve melhor desempenho na classificação, referindo valores como precisão de 1,00 e F1-Score de 0,97. Também comentou a regressão para previsão de NO2, referindo valores de R2 aproximadamente entre 0,70 e 0,71, o que foi interpretado como capacidade preditiva moderada.

Esta variante é a melhor para justificar a componente científica do projecto, porque liga diretamente os alertas do Módulo 1 às métricas do Módulo 2. No entanto, pode gerar textos mais densos e menos acessíveis ao cidadão comum.

---

### Pontos fortes da Prompt 3

A principal vantagem da Prompt 3 foi a organização. Como a estrutura estava claramente definida, a IA produziu respostas mais fáceis de converter em PDF e mais simples de avaliar.

Outro ponto forte foi a consistência entre relatórios. Todos os outputs seguiram uma lógica semelhante, permitindo comparar alertas diferentes com base nas mesmas dimensões de análise.

A Prompt 3 também ajudou a garantir que a secção de limitações e riscos éticos aparecesse sempre no relatório. Isto é importante porque a professora pediu explicitamente uma análise crítica sobre transparência, enviesamentos e possíveis alucinações.

Além disso, esta prompt aumentou a probabilidade de a IA usar os dados quantitativos fornecidos, como número de ocorrências, percentagem de ocorrência e métricas do Módulo 2, porque estes elementos estavam associados a secções específicas do relatório.

---

### Limitações da Prompt 3

Apesar de ser mais organizada, a Prompt 3 pode tornar o output mais rígido. Como a IA segue uma estrutura fixa, a resposta pode parecer menos natural ou menos criativa.

Outra limitação é que a prompt pode gerar textos repetitivos entre PDFs. Como todos os alertas seguem as mesmas secções, algumas frases sobre ética, validação humana ou riscos de automação podem tornar-se semelhantes.

Também existe o risco de a IA preencher todas as secções mesmo quando existem poucos dados para um determinado alerta. Por exemplo, no caso de alertas com poucas ocorrências, como `risco_nevoeiro`, a IA pode produzir uma análise extensa apesar da baixa amostragem. Isto exige revisão humana para garantir que a interpretação é proporcional aos dados disponíveis.

---

### Conclusão da análise da Prompt 3

A Prompt 3 foi eficaz para gerar outputs mais organizados, consistentes e adequados à criação de PDFs.

A técnica de structured prompting mostrou-se especialmente útil porque permitiu transformar dados técnicos em relatórios com uma estrutura clara e repetível. Isto facilitou a comparação entre alertas e garantiu que os elementos obrigatórios do Módulo 3 fossem incluídos.

No entanto, esta abordagem pode reduzir a flexibilidade da resposta e gerar alguma repetição entre relatórios. Por isso, a melhor solução foi combinar esta técnica com instruções adicionais da prompt original, como a obrigação de usar dados concretos, evitar Markdown e incluir sempre uma análise crítica dos riscos éticos.

Em suma, a Prompt 3 é uma das mais adequadas para este projecto, porque aproxima a geração automática da IA das exigências formais da entrega final.

---

# Comparação entre as três variantes de prompt

A primeira prompt, estruturada multi-perspectiva, foi a mais equilibrada. Produziu relatórios completos, com as quatro perspetivas pedidas e com uma organização consistente entre todos os PDFs.

A segunda prompt, orientada para comunicação pública, foi mais clara e acessível. Ajudou a transformar dados técnicos em recomendações práticas para cidadãos, mas reduziu o detalhe técnico das métricas.

A terceira prompt, técnico-estratégica, foi a mais forte para análise académica. Deu mais importância às métricas dos modelos, à distinção entre dados observados e previsões, e à validação humana. Contudo, é menos simples para leitura pública.

Assim, a melhor estratégia para o projecto foi combinar as três abordagens: usar uma estrutura fixa, incluir perspectivas diferentes e obrigar a IA a fundamentar o relatório com dados quantitativos.

---

# Análise Geral dos Outputs dos PDFs

## Cobertura dos alertas

Foram gerados relatórios PDF para os principais tipos de alerta presentes no `alert_results.csv`, incluindo:

- `frio_extremo`;
- `humidade_baixa`;
- `ozono_alto`;
- `particulas_pm10_altas`;
- `particulas_pm25_altas`;
- `poluicao_no2_alta`;
- `risco_calor_extremo`;
- `risco_incendio_moderado`;
- `risco_nevoeiro`.

Esta abordagem cumpre o objectivo definido para o Módulo 3: gerar um relatório separado por tipo de alerta, com várias perspectivas e com uma secção de limitações e riscos éticos.

## Alertas mais relevantes

O alerta `poluicao_no2_alta` foi o mais frequente, com 5702 ocorrências, representando 52,95% dos registos analisados. Este resultado indica que a poluição por NO2 é o problema mais recorrente no conjunto de dados e deve ser tratado como uma prioridade de gestão urbana.

O alerta `humidade_baixa` também teve uma frequência elevada, com 2217 ocorrências e 20,59% dos registos. Este alerta foi associado a riscos de secura ambiental, incêndio e degradação da qualidade do ar.

O alerta `frio_extremo` teve 1176 ocorrências, correspondendo a 10,92% dos registos, demonstrando relevância para políticas de apoio a populações vulneráveis.

O alerta `risco_incendio_moderado` surgiu em 888 ocorrências, ou 8,25% dos registos, sendo importante para vigilância preventiva em zonas verdes e gestão de riscos ambientais.

Alertas como `ozono_alto`, `particulas_pm10_altas` e `risco_nevoeiro` foram menos frequentes, mas continuam relevantes porque podem afectar directamente a saúde pública, a mobilidade e a segurança rodoviária.

## Qualidade dos outputs

Os PDFs apresentam uma estrutura consistente, normalmente dividida em oito secções:

1. Resumo Executivo;
2. Dados Observados no Sistema;
3. Perspectiva do Cidadão;
4. Perspectiva da Protecção Civil;
5. Perspectiva do Presidente da Câmara;
6. Perspectiva do Técnico de Dados Municipal;
7. Limitações e Riscos Éticos;
8. Conclusão.

Esta estrutura facilita a leitura e mostra capacidade de adaptação da IA generativa a diferentes públicos. A perspectiva do cidadão usa linguagem simples e recomendações práticas. A perspectiva da Protecção Civil foca-se na resposta operacional. A perspectiva do Presidente da Câmara apresenta recomendações estratégicas. A perspectiva do Técnico de Dados Municipal interpreta os dados e métricas dos modelos.

## Integração dos Módulos 1, 2 e 3

Os relatórios mostram uma boa integração entre os três módulos do projecto.

O Módulo 1 fornece os alertas e as acções recomendadas.
O Módulo 2 fornece as métricas dos modelos de classificação e regressão.
O Módulo 3 transforma esses resultados em relatórios interpretáveis, adaptados a diferentes públicos.

Esta integração é especialmente visível em relatórios como `risco_calor_extremo`, onde são apresentados dados ambientais médios, acções recomendadas e métricas do modelo Random Forest Classifier. Também é visível no relatório `risco_nevoeiro`, que reconhece a baixa frequência do evento e alerta para a possibilidade de enviesamento por baixa amostragem.

## Pontos fortes dos outputs

Os principais pontos fortes dos PDFs são:

- utilização de dados quantitativos reais;
- organização clara por secções;
- adaptação do discurso a diferentes públicos;
- inclusão de recomendações práticas e estratégicas;
- referência a métricas de machine learning;
- inclusão de riscos éticos e necessidade de validação humana.

## Limitações observadas

Apesar da boa qualidade geral, existem algumas limitações:

Apesar da boa qualidade geral, existem algumas limitações:

- a IA por vezes usa interpretações fortes a partir de poucos dados, como no caso de `risco_nevoeiro`, que tem apenas 4 ocorrências;
- alguns relatórios apresentam métricas do Módulo 2 de forma repetida, sem as relacionar directamente com o alerta específico;
- em certos casos, a IA pode afirmar ausência de alguns dados ambientais, mesmo quando o dataset pode conter essas colunas;
- o estilo linguístico nem sempre é totalmente uniforme entre PDFs;
- a IA pode transformar métricas em conclusões demasiado confiantes, pelo que a revisão humana continua indispensável.

# Secção Ético-Crítica

## Enquadramento

A utilização de IA generativa no Módulo 3 permitiu transformar dados técnicos dos Módulos 1 e 2 em relatórios compreensíveis para diferentes públicos, como cidadãos, Protecção Civil, Presidente da Câmara e técnicos municipais.

Apesar desta utilidade, é importante reconhecer que a IA generativa não deve ser usada como uma fonte absoluta de verdade. Os relatórios produzidos devem ser vistos como documentos de apoio à decisão e não como decisões finais.

---

## Transparência

A transparência é essencial quando se utilizam sistemas de IA em contexto urbano e ambiental.

Neste projecto, os relatórios foram gerados a partir de dados provenientes do `alert_results.csv` e do `metrics.csv`. No entanto, o processo de geração de texto depende de um modelo externo de IA, cujo funcionamento interno não é totalmente visível para o utilizador.

Por isso, é importante deixar claro:

- que os textos foram gerados com apoio de IA generativa;
- que os dados usados vêm dos módulos anteriores;
- que as conclusões devem ser revistas por humanos;
- que o modelo pode reorganizar ou interpretar os dados de forma não totalmente previsível.

A transparência aumenta a confiança dos utilizadores e permite que cidadãos e decisores compreendam melhor os limites do sistema.

---

## Enviesamentos nos dados

Os resultados gerados pela IA dependem directamente da qualidade dos dados de entrada.

Se os dados ambientais tiverem falhas, valores extremos, sensores mal calibrados ou cobertura desigual entre zonas da cidade, os relatórios também podem reflectir essas limitações.

Por exemplo, se existirem mais sensores numa zona urbana com muito tráfego do que numa zona periférica, o sistema pode dar maior importância aos problemas dessa zona e sub-representar outras áreas da cidade.

Isto pode gerar enviesamentos na análise e influenciar recomendações futuras. Assim, os dados devem ser avaliados regularmente, garantindo que representam a cidade de forma justa e equilibrada.

---

## Risco de alucinações da IA

Um dos principais riscos da IA generativa é a possibilidade de produzir afirmações incorrectas, exageradas ou não suportadas pelos dados. Este fenómeno é conhecido como alucinação.

Mesmo quando a prompt pede explicitamente para não inventar valores, a IA pode:

- interpretar uma correlação como se fosse causalidade;
- apresentar conclusões demasiado fortes;
- preencher lacunas com explicações plausíveis, mas não confirmadas;
- dar mais confiança aos resultados do que os dados justificam.

Por isso, todos os relatórios gerados devem ser revistos antes de serem usados em contexto real.

No caso deste projecto, a revisão humana é especialmente importante porque os relatórios abordam temas sensíveis como saúde pública, mobilidade, poluição, risco de incêndio, frio extremo e segurança rodoviária.

---

## Dependência excessiva de automação

Outro risco importante é a dependência excessiva de sistemas automáticos.

A IA pode ajudar a resumir dados, organizar informação e adaptar a comunicação a diferentes públicos, mas não deve substituir especialistas humanos.

Decisões sobre evacuações, restrições de tráfego, avisos à população, alocação de equipas de emergência ou políticas públicas devem continuar a ser tomadas por pessoas qualificadas, com conhecimento técnico e contexto local.

O sistema deve funcionar como apoio à decisão, não como substituto da decisão humana.

---

## Falsos positivos e falsos negativos

Nos sistemas de alerta, os erros podem ter consequências importantes.

Um falso positivo acontece quando o sistema indica um alerta que, na realidade, não representa um risco significativo. Isto pode causar desperdício de recursos, alarmismo e perda de confiança por parte da população.

Um falso negativo acontece quando o sistema não identifica um risco real. Este caso pode ser ainda mais grave, porque pode deixar cidadãos e serviços de emergência desprevenidos.

Por isso, os resultados devem ser sempre cruzados com validação humana, observação no terreno e outros dados disponíveis.

---

## Responsabilidade humana

A responsabilidade final pelas decisões não deve ser atribuída à IA.

Mesmo que o relatório seja gerado automaticamente, cabe aos técnicos, decisores e entidades responsáveis confirmar se:

- os dados estão correctos;
- as conclusões fazem sentido;
- as recomendações são proporcionais;
- a informação é adequada ao público-alvo;
- não existem riscos de má interpretação.

A IA generativa deve ser usada como ferramenta auxiliar, mantendo sempre supervisão humana.

---

## Privacidade e segurança dos dados

Embora este projecto trabalhe com dados ambientais e não com dados pessoais directos, continua a ser importante garantir boas práticas de segurança.

A chave da API usada no Módulo 3 deve ficar num ficheiro `.env`, que não deve ser enviado para repositórios públicos. Isto evita exposição indevida da conta usada para chamar o modelo externo de IA.

Além disso, qualquer sistema real de cidade inteligente deve ter especial cuidado caso venha a integrar dados sensíveis, como localização de cidadãos, mobilidade individual ou dados de saúde.

---

## Avaliação crítica dos PDFs gerados

Os PDFs gerados demonstram que a IA generativa consegue adaptar a mesma informação a diferentes públicos. A perspectiva do cidadão tornou os alertas mais acessíveis, a perspectiva da Protecção Civil destacou a resposta operacional, a perspectiva do Presidente da Câmara focou-se em políticas públicas e a perspectiva do Técnico de Dados Municipal analisou métricas e limitações.

No entanto, também se observam limitações. Alguns relatórios podem repetir expressões semelhantes, sobretudo nas secções de ética e validação humana. Além disso, quando um alerta tem poucas ocorrências, como `risco_nevoeiro`, a IA pode produzir uma análise extensa apesar da baixa quantidade de dados disponíveis.

Isto mostra que os outputs são úteis, mas exigem revisão crítica.

---

## Conclusão Ético-Crítica

O Módulo 3 mostra o potencial da IA generativa para apoiar a comunicação de riscos ambientais numa cidade sustentável. A tecnologia permite transformar dados técnicos em relatórios claros, estruturados e adaptados a diferentes públicos.

Contudo, a utilização deste tipo de sistema deve ser acompanhada por princípios de transparência, validação humana, responsabilidade, controlo de enviesamentos e cuidado com possíveis alucinações.

Assim, a IA generativa deve ser entendida como uma ferramenta de apoio à comunicação e à decisão, mas nunca como substituto de especialistas humanos ou de processos institucionais de validação.

---

## Avaliação crítica final

No geral, os PDFs gerados cumprem bem o objectivo do Módulo 3. A IA generativa foi usada para sintetizar os resultados dos módulos anteriores, gerar recomendações e adaptar a comunicação a vários públicos.

A maior vantagem observada foi a capacidade da IA em transformar dados técnicos em textos úteis para diferentes actores da cidade. No entanto, os outputs não devem ser tratados como decisão final. Devem ser considerados documentos de apoio, sujeitos a validação humana, revisão técnica e confirmação dos dados originais.

Assim, o Módulo 3 demonstra o potencial da IA generativa como ferramenta de comunicação e apoio à decisão em cidades sustentáveis, mas também evidencia riscos importantes como enviesamentos, alucinações e dependência excessiva de automação.


# Prompts usados no Módulo 3

## Prompt multi-perspectiva

```text
Actua como um sistema de Inteligência Urbana para uma cidade sustentável.

Recebeste resultados de dois módulos de um projecto académico:

DADOS DO MÓDULO 1 — SISTEMA DE REGRAS
Total de registos analisados: 10768

Alertas mais frequentes:
alertas
poluicao_no2_alta          5702
sem alerta                 3637
humidade_baixa             2217
frio_extremo               1176
risco_incendio_moderado     888
risco_calor_extremo         421
particulas_pm25_altas       359
ozono_alto                   57
particulas_pm10_altas        17
risco_nevoeiro                4

DADOS DO MÓDULO 2 — MODELOS DE MACHINE LEARNING
Métricas dos modelos:
                  Modelo          Tarefa  Accuracy  Precision   Recall  F1-Score      MAE     RMSE       R2
     Regressao Logistica   Classificacao  0.928849   0.887916 0.887916  0.887916      NaN      NaN      NaN
Random Forest Classifier   Classificacao  0.981656   1.000000 0.942207  0.970243      NaN      NaN      NaN
        Regressao Linear Regressao (NO2)       NaN        NaN      NaN       NaN 5.114810 6.716574 0.716206
 Random Forest Regressor Regressao (NO2)       NaN        NaN      NaN       NaN 5.358155 6.884418 0.701845


Com base nestes dados, gera um relatório em português de Portugal, claro e bem estruturado.

Gera um relatório em português de Portugal para o alerta {Aparece aqui um tipo de alerta que aparece no alert_results.csv com exceção "sem_alerta"}.

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
```

### Relatório do Alerta: frio_extremo

---

### **1. Resumo Executivo**

O alerta de frio extremo sinaliza um evento meteorológico de relevância para a cidade, caracterizado por
temperaturas significativamente baixas que podem impactar a saúde pública, a infraestrutura urbana e a rotina
diária dos cidadãos. Este tipo de ocorrência exige uma monitorização atenta e a implementação de medidas
preventivas e reativas por parte das autoridades municipais. De acordo com os dados analisados, o alerta de frio
extremo foi registado em 1176 das 10768 ocorrências monitorizadas pelo sistema, representando 10.92% do
total. Esta percentagem sublinha a sua frequência considerável, indicando que não se trata de um evento isolado,
mas sim de um desafio recorrente que a cidade deve preparar-se para enfrentar de forma eficaz e sustentável,
minimizando riscos e protegendo a população

---

### **2. Perspetiva do Cidadão**

Para o cidadão comum, um alerta de frio extremo traduz-se em mudanças e cuidados acrescidos no seu
dia-a-dia. As baixas temperaturas podem causar desconforto generalizado, aumentar o risco de doenças
respiratórias e hipotermia, especialmente em grupos mais vulneráveis como idosos e crianças. A locomoção
pode tornar-se mais perigosa devido à formação de gelo nas estradas e passeios. Os custos com o aquecimento
das habitações tendem a aumentar, exigindo uma gestão atenta do consumo de energia.

Para sua segurança e saúde, aconselha-se a vestir várias camadas de roupa, mantendo o corpo quente e seco.
Hidrate-se bem com bebidas quentes e evite esforços físicos desnecessários ao ar livre. Verifique o estado de
saúde de vizinhos e familiares idosos ou doentes. Proteja os canos de água da sua casa para evitar o seu
congelamento e rutura. Em caso de necessidade de deslocação, conduza com extrema prudência e esteja atento
aos avisos das autoridades.

---

### **3. Perspetiva da Protecção Civil**

A Protecção Civil deve ativar de imediato o Plano Municipal de Emergência para o frio extremo, mobilizando os
recursos humanos e materiais necessários. Isto inclui a abertura e gestão de abrigos de emergência aquecidos, a
distribuição de cobertores e refeições quentes, e o reforço das equipas de saúde para atendimento a casos de
hipotermia ou problemas respiratórios. É crucial disseminar informações claras e contínuas à população sobre as
medidas de autoproteção e os contactos de emergência. A monitorização da infraestrutura crítica, como a rede
de abastecimento de água e eletricidade, também é prioritária.

A análise de alertas como o frio extremo comporta riscos de falsos positivos e falsos negativos. Falsos positivos
podem ocorrer quando o sistema emite um alerta com base em previsões que não se concretizam na sua
totalidade, levando a uma mobilização excessiva de recursos e à eventual desensibilização do público. Falsos
negativos são mais perigosos, ocorrendo quando o sistema falha em detetar uma situação de risco iminente,
resultando numa falta de preparação e aumentando a vulnerabilidade da população e a perda de credibilidade do
sistema. É essencial calibrar os modelos para otimizar a precisão.

---

### **4. Perspetiva do Presidente da Câmara**

Senhores munícipes, o alerta de frio extremo exige uma resposta coordenada e estratégica que garanta a
segurança e o bem-estar de todos. Face à reincidência deste fenómeno, refletida nos nossos dados, proponho as
seguintes recomendações de ação para a nossa cidade.

Primeiro, devemos reforçar os programas de apoio social, garantindo que os mais vulneráveis, em particular a
população sem-abrigo e os idosos isolados, tenham acesso a abrigos aquecidos, alimentação e cuidados de
saúde adequados. A solidariedade e a proteção social são pilares da nossa cidade sustentável.

Segundo, é fundamental investir na resiliência das nossas infraestruturas críticas. Isto inclui a modernização da
rede de abastecimento de água para prevenir roturas por congelamento e a promoção de programas de
eficiência energética nos edifícios públicos e privados, tornando a cidade mais robusta face às adversidades
climáticas.

Terceiro, impulsionar a comunicação transparente e eficaz com os cidadãos. É imperativo que a informação
sobre o alerta e as medidas preventivas chegue a todos, através de múltiplos canais, capacitando cada munícipe
a agir de forma informada e responsável.

---

### **5. Perspetiva do Técnico de Dados Municipal**

A ocorrência de frio extremo, representando 10.92% do total de 10768 registos analisados, indica que este é um
evento significativo e recorrente no contexto urbano. Este valor sugere que, embora não seja diário, o frio
extremo é suficientemente frequente para justificar a manutenção e melhoria contínua dos planos de
contingência específicos. A análise desta percentagem permite-nos aferir a escala do problema e priorizar
recursos de acordo com a sua prevalência.

Contudo, existem limitações inerentes aos dados apresentados. A ausência de contexto temporal impede-nos de
compreender se esta percentagem é estável, crescente ou decrescente ao longo do tempo (ex: anualmente,
sazonalmente). Não temos dados sobre a severidade exata de cada ocorrência de frio extremo (ex: temperatura
mínima atingida, duração do período de frio). Adicionalmente, não foram fornecidos dados sobre os impactos
resultantes destes alertas (ex: número de hospitalizações, danos em infraestruturas), o que limita a avaliação
completa da sua criticidade. A natureza do "total de registos no ficheiro" também não está totalmente
especificada, dificultando a contextualização exata da amostra.

---

### **6. Limitações e Riscos Éticos**

A atuação de um sistema de Inteligência Urbana, mesmo com dados robustos, está sujeita a importantes
limitações e riscos éticos. A transparência na recolha, processamento e interpretação dos dados é crucial. Os
cidadãos e as partes interessadas devem compreender como as decisões são tomadas e quais os critérios
subjacentes. A opacidade pode levar à desconfiança e à falta de adesão às medidas propostas.

Existe o risco de enviesamentos nos dados. Se os dados históricos que alimentam o sistema refletirem
desigualdades sociais ou geográficas, as recomendações da IA podem inadvertidamente perpetuar ou amplificar
essas disparidades, por exemplo, ao focar recursos em áreas que historicamente já recebem mais atenção. É
fundamental garantir que os conjuntos de dados são representativos e que os algoritmos são projetados para
mitigar vieses.

Outro risco é o das possíveis alucinações da IA, onde o sistema pode gerar informações ou recomendações que,
embora plausíveis, não correspondem à realidade dos factos ou excedem as capacidades dos dados disponíveis.
Isso pode resultar em decisões inadequadas ou na implementação de medidas ineficazes ou até prejudiciais.

Por fim, a necessidade de validação humana é incontornável. A Inteligência Urbana deve ser uma ferramenta de
apoio à decisão, e não um substituto para a experiência e o discernimento de especialistas humanos em áreas
como a meteorologia, a proteção civil, a saúde pública e o planeamento urbano. A intervenção humana é vital
para contextualizar os dados, aplicar o bom senso e assumir a responsabilidade final pelas ações.
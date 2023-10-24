# Previsão de preço de ações bancárias

## 1. Definição do problema
No quadro de regressão supervisionada usado para este projeto, a variável prevista é o retorno semanal das ações da JPM (JPMorgan Chase & Co.). Precisamos identificar o preço da ação da JPM no próximo dia dado os valores anteriores para que podemos analisar o risco e lucrabilidade antes mesmo de realmente injetar capital nesse ativo. 


## 2. Sobre os dados
As informações empregadas nesta iniciativa foram obtidas através da extração de dados do Yahoo Finance, abrangendo as ações e quanto as taxas de câmbio e dos índices, foram obtidos no FRED (Federal Reserve Bank) e é importante ressaltar que estaremos utilizado dados da cotação no fechamento diário. O escopo temporal também desempenha um papel relevante, e para isso, coletaremos dados abrangendo o intervalo de janeiro de 2010 a dezembro de 2022, abrangendo dias completos de ambos os meses finais.

Para este projeto, além dos dados históricos da JPM, as variáveis independentes utilizadas são as seguintes ativos potencialmente correlacionados:

- Ações:
   - Bank of America Corporation (BAC) e Wells Fargo & Company (WFC)
- Taxa de câmbio:
   - USD/UK e USD/EUR
- Índices:
   - S&P 500, Dow Jones e VIX

Após a conclusão do processo de coleta e as devidas etapas de limpeza, incluindo a remoção de dados faltantes, o conjunto de dados resultante será composto por oito colunas, sendo que o nome de cada coluna corresponde ao ticker que identifica cada um dos ativos.

## 3. Análise dos dados

### 3.1. Mostra dos dados
A tabela apresentada abaixo compreende os resultados derivados de uma coleta de dados minuciosa, reunindo informações cruciais referentes aos valores das ações de diversos bancos, indicadores de mercado selecionados e, por fim, as cotações cambiais entre o dólar e as moedas britânica e europeia.

A série de dados abrange um período abrangente, estendendo-se do ano de 2013 até o ano de 2022. Contudo, é imperativo salientar que o conjunto de informações pode ter sofrido algumas exclusões ao longo do processamento, motivadas pela detecção de valores ausentes. Nesse sentido, foi conduzida uma etapa de depuração dos dados, visando à eliminação de quaisquer registros que pudessem conter lacunas informacionais.

|      Dates |        JPM |       BAC |       WFC | DEXUSUK | DEXUSEU |  SP500 |     DJIA | VIXCLS |
|-----------:|-----------:|----------:|----------:|--------:|--------:|-------:|---------:|-------:|
| 2013-08-23 |  39.576180 | 12.223401 | 32.090580 |  1.5578 |  1.3392 | 1663.5 | 15010.51 |  13.98 |
| 2022-12-30 | 131.179276 | 32.646065 | 40.393898 |  1.2077 |  1.0698 | 3839.5 | 33147.25 |  21.67 |

### 3.2. Resumo dos dados
A tabela anterior é feito o resumo numérico de cada variável dos dados, alguns pontos importantes para se destacar da tabela:
- A média do do preço da ação de JPM (JPMorgan Chase) é de aproximadamente 85.66, com um desvio padrão de 34.20.
- A média do do preço da ação de BAC (Bank of America) é cerca de 23.42, com um desvio padrão de 9.35.
- A média do do preço da ação de WFC (Wells Fargo) é de cerca de 41.02, com um desvio padrão de 6.92.
- Há diferenças notáveis nas médias dos diferentes bancos (JPM, BAC, WFC), sugerindo que eles podem ter diferentes níveis de desempenho ou tamanho no mercado financeiro.
- O DJIA (Dow Jones Industrial Average) tem um valor mínimo de 14776.13 e máximo de 36799.65, indicando a faixa de flutuação do índice ao longo do período.
- O VIXCLS (Índice de Volatilidade CBOE) tem um valor mínimo de 9.14 e máximo de 82.69, mostrando a gama de volatilidade percebida nos mercados financeiros.

### 3.3. Comportamento da variável alvo (JPM)
A imagem abaixo disponibiliza a visualização dos preços da ação da variável alvo ao decorrer do tempo, e assim podemos identificar a sua tendência e sazonalidade.

![image info](./reports/images/jpm_stocks.png)

### 3.4. Relação variável alvo e ativos
#### 3.4.1. Bancos

![image info](./reports/images/jpm_wfc_bac.png)

É notável e relevante observar que nos gráficos anteriores, há uma clara comparação entre o preço da ação que será objeto de previsão (no caso, JPM) com os preços das ações de seus concorrentes (BAC e WFC). Uma análise mais detalhada revela padrões notáveis de comportamento entre JPM e BAC, indicando uma certa similaridade em suas trajetórias de preço ao longo do tempo. Isso pode sugerir uma correlação ou influências compartilhadas entre esses dois ativos, possivelmente devido a fatores do setor financeiro ou condições econômicas mais amplas.

Além disso, a diferença entre JPM e WFC, apesar de notável em termos de valores absolutos, destaca uma tendência semelhante em termos de padrões de aumento ou queda. Essa semelhança na direção das flutuações pode indicar uma sensibilidade compartilhada a eventos macroeconômicos ou fatores do mercado que afetam ambos os ativos de maneira semelhante.

#### 3.4.2. Taxa de câmbio

![image info](./reports/images/jpm_currencies.png)

É possível notar que as cotações entre dólares, libras e euros podem apresentar desafios na extração imediata de informações impactantes, devido à complexidade de fatores que influenciam as taxas de câmbio. Dado o caráter multifacetado das dinâmicas cambiais, a abordagem de análise pode se estender para além de observações visuais diretas.

Explorar métodos adicionais, como análise de correlação, testes de hipóteses e algoritmos de machine learning, pode ser uma abordagem promissora para desvendar padrões e relações subjacentes nos dados cambiais. A análise de correlação pode revelar graus de associação entre as diferentes taxas de câmbio, ajudando a identificar se há momentos em que elas se movem de forma coordenada ou divergente.

#### 3.4.3. Índices

![image info](./reports/images/jpm_indicies.png)

O insight aqui é que existe uma possibilidade de que os indíces SP500, DJIA e VIXCLS sejam capaz de auxiliar na predição, dado que os comportamentos estão alinhados, portanto o uso dessas variável podem vir ser essencial para o projeto.

## 3.5. Correlação

![image info](./reports/images/correlacao.png)

Olhando o gráfico de correlação, podemos identificar uma alta correlação positiva entre a variável alvo (JPM) com os indíces, e também uma correlação negativa com as taxas de câmbios. 

CONTINUAR A CRIAR AQUI
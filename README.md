
# PySpark
É o apache spark, ferramenta de Big data para processar grandes volumes de dados 
rodando em Python 

```python

!apt-get update -qq
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
!wget -q https://archive.apache.org/dist/spark/spark-3.1.2/spark-3.1.2-bin-hadoop2.7.tgz
!tar xf spark-3.1.2-bin-hadoop2.7.tgz
!pip install -q findspark

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master('local[*]') \
    .appName("Iniciando com Spark") \
    .config('spark.ui.port', '4050') \
    .getOrCreate()

```

## DataFrames com Spark


### Interfaces Spark

Existem três interfaces principais do Apache Spark que você deve conhecer: Resilient Distributed Dataset, DataFrame e Dataset.

- **Resilient Distributed Dataset**: A primeira abstração do Apache Spark foi o Resilient Distributed Dataset (RDD). É uma interface para uma sequência de objetos de dados que consiste em um ou mais tipos localizados em uma coleção de máquinas (um cluster). Os RDDs podem ser criados de várias maneiras e são a API de “nível mais baixo” disponível. Embora esta seja a estrutura de dados original do Apache Spark, você deve se concentrar na API DataFrame, que é um superconjunto da funcionalidade RDD. A API RDD está disponível nas linguagens Java, Python e Scala.

- **DataFrame**: Trata-se de um conceito similar ao DataFrame que você pode estar familiarizado como o pacote pandas do Python e a linguagem R . A API DataFrame está disponível nas linguagens Java, Python, R e Scala.

- **Dataset**: uma combinação de DataFrame e RDD. Ele fornece a interface digitada que está disponível em RDDs enquanto fornece a conveniência do DataFrame. A API Dataset está disponível nas linguagens Java e Scala.

Em muitos cenários, especialmente com as otimizações de desempenho incorporadas em DataFrames e Datasets, não será necessário trabalhar com RDDs. Mas é importante entender a abstração RDD porque:

- O RDD é a infraestrutura subjacente que permite que o Spark seja executado com tanta rapidez e forneça a linhagem de dados.

- Se você estiver mergulhando em componentes mais avançados do Spark, pode ser necessário usar RDDs.

- As visualizações na Spark UI fazem referência a RDDs.





















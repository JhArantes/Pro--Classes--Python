
<<<<<<< HEAD
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




















=======
# 🧠 Introdução às Classes em Python

Quando falamos em **classes**, estamos entrando no universo da **Programação Orientada a Objetos (POO)**.

Na POO, **objetos** são estruturas que representam **coisas do mundo real**, unindo **atributos** (características) e **métodos** (ações/comportamentos). Um **objeto** pode ser, por exemplo, um carro, um usuário ou um produto.

---

## 🧱 O que é uma Classe?

Uma **classe** é como um **molde** (ou modelo) para criar objetos. Ela define:
- **Atributos**: características do objeto
- **Métodos**: ações que o objeto pode executar

A partir de uma classe, podemos criar **instâncias** (objetos reais) com comportamentos definidos.

---

## 🧪 Exemplo básico

```python
class Carro:
    def __init__(self, pneu, ano, cor):
        self.pneu = pneu
        self.ano = ano
        self.cor = cor

    def calcular_preco(self):
        total = 0
        if self.pneu == "Impecavel":
            total += 200
        else:
            total += 100
        return total
```

### 🛠 Criando um objeto (instância)

```python
meu_carro = Carro("Impecavel", 2020, "Preto")
print(meu_carro.calcular_preco())  # Saída: 200
```

---

# 🔎 Aprofundando...

## 📌 O que é `self`?

O `self` representa a **instância atual** da classe. Ele é necessário para acessar os atributos e métodos do próprio objeto.

```python
self.cor = cor  # Armazena a cor no atributo da instância
```

---

## 🧠 Encapsulamento

**Encapsulamento** significa proteger os dados internos da classe e permitir acesso controlado.

```python
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # atributo privado

    def ver_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
```

---

## 🔁 Herança

Permite que uma classe **herde** atributos e métodos de outra.

```python
class Veiculo:
    def __init__(self, cor):
        self.cor = cor

class Moto(Veiculo):
    def buzinar(self):
        print("Biiiiii")
```

---

## 🎯 Polimorfismo

Diferentes classes podem implementar o mesmo método de maneiras distintas.

```python
class Cachorro:
    def falar(self):
        print("Au Au")

class Gato:
    def falar(self):
        print("Miau")

for animal in [Cachorro(), Gato()]:
    animal.falar()
```

---

# ✅ Conclusão

- **Classe** é um molde para criar objetos
- **Objeto** é uma instância da classe
- **Atributos** são características dos objetos
- **Métodos** são comportamentos
- **POO** permite escrever códigos organizados, reutilizáveis e robustos

---

💡 *Dominar classes e POO é essencial para qualquer programador que deseja escrever códigos limpos e reutilizáveis!*
>>>>>>> a5efcdc30fea5fabbcbeb00cd742464b2de18e26

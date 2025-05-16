
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

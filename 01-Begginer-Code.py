
class personagem:
    def __init__(self, health, speed, damage):
        self.health = health
        self.speed = speed
        self.damage = damage

    def dobro_speed(self):
        self.speed *= 2


tank = personagem(200, 50, 50)
ninja = personagem(80, 100, 75)

print('=================\n')
print(f'O tank tem {tank.speed} Velocidade')
print(f'O ninja tem {ninja.speed} Velocidade')


ninja.dobro_speed()


print('=================\n Apos o Doble \n=================')
print(f'O tank tem {tank.speed} Velocidade')
print(f'O ninja tem {ninja.speed} Velocidade')


































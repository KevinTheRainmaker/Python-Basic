# 클래스를 사용하는 이유

# 1) 클래스를 사용하지 않았을 때
monster1_name = '미노타우로스'
monster1_health = 15000
monster1_attack = 700

print(f'몬스터명: {monster1_name}')

monster2_name = '바실리스크'
monster2_health = 33000
monster2_attack = 2100

print(f'몬스터명: {monster2_name}')

def basic_attack(name, attack):
    print(f'{name}의 기본 공격력: {attack}')

basic_attack(monster1_name, monster1_attack)
basic_attack(monster2_name, monster2_attack)



# 2) 클래스를 사용하는 경우

class Monster:
    def basic_attack(self):
        print(f'{self.name}의 기본 공격력: {self.attack}')

    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        print(f'몬스터명: {name}')
        self.basic_attack()
        print('')

mino = Monster('미노타우로스', 15000, 700)
basil = Monster('바실리스크', 33000, 2100)

# 새로운 몬스터(객체)를 추가하게 될 경우 클래스를 사용하는 편이 압도적으로 편리하다.
zomb = Monster('좀비', 1000, 200)
skul = Monster('스켈레톤', 1100, 400)

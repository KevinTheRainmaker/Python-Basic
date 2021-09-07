# 생성자(__init__) 함수: 인스턴스를 만들 때 가장 먼저, 반드시 호출되는 메서드
# self 파라미터: 인스턴스 스스로를 지칭

class Monster:
    def __init__(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed
    
    def decrease_health(self, num):
        self.health -= num
    
    def get_health(self):
        return self.health

    def basic_attack(self):
        # health에 따라 공격력이 변동
        # 최대 기본 공격력은 자체 공격력을 넘지 않음
        attack_point = self.attack * self.speed
        rage_point = attack_point // self.health

        basic_attack = (attack_point + rage_point) % self.attack
        
        if basic_attack == 0:
            basic_attack = self.attack

        print(basic_attack)

# 고블린 인스턴스
goblin = Monster(800, 120, 300)

print(goblin.get_health())
goblin.basic_attack()

goblin.decrease_health(100)
print(goblin.get_health()) # 감소한 값을 가져옴
goblin.basic_attack()

goblin.decrease_health(600)
print(goblin.get_health())
goblin.basic_attack()

# 웨어울프 인스턴스
warewolf = Monster(2100, 800, 1100)

print(warewolf.get_health())
warewolf.basic_attack()
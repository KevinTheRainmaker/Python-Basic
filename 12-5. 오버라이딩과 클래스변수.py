import random

# 12-4
class Monster:
    max_num = 1000 # 클래스 변수: 모든 인스턴스들이 공유하는 변수

    def __init__(self, name, health, attack, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.speed = speed
        Monster.max_num -= 1

    def decrease_health(self, num):
        self.health -= num
    
    def get_health(self):
        return self.health

    def basic_attack(self):
        attack_point = self.attack * self.speed
        rage_point = attack_point // self.health

        basic_attack = (attack_point + rage_point) % (self.attack + self.speed)
        
        if basic_attack == 0:
            basic_attack = self.attack

        print(f'{self.name}의 기본공격! - {basic_attack}')
    
    def background(self):
        background = '땅'
        print(f'{self.name}의 서식지: {background}')

class Warewolf(Monster):
    pass

class Shark(Monster):
    def background(self):
        background = '바다'
        print(f'{self.name}의 서식지: {background}')

# 드래곤에 스킬을 3개 추가하여 이 중 랜덤으로 나가게 해보자.
# 부모 클래스에 skill 속성을 추가하면 스킬이 없는 웨어울프와 샤크에게는 필요없는 속성이 상속되므로 적절하지 않다.

class Dragon(Monster):
    def __init__(self, name, health, attack, speed): # 생성자 오버라이딩
        super().__init__(name, health, attack, speed) # super로 부모클래스 호출
        self.skills = ('화염방사','드래곤테일','드래곤스톰')

    def background(self):
        background = '하늘'
        print(f'{self.name}의 서식지: {background}')

    def skill(self):
        print(f'{self.name}의 {self.skills[random.randint(0,2)]}!')

dragon = Dragon('크라드메서', 10000, 4200, 2700)

dragon.skill()

# max_num 공유 확인
print(dragon.max_num)

warewolf = Warewolf('웨어울프', 2100, 800, 1100)
print(dragon.max_num)

shark = Shark('샤크', 3000, 1000, 2000)
print(dragon.max_num) # dragon 인스턴스의 max_num을 확인하고 있지만, 공유가 되기 때문에 인스턴스 호출 시 마다 계속 줄어들고 있음을 확인할 수 있다.

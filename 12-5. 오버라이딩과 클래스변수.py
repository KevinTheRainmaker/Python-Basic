# 12-4
class Monster:
    def __init__(self, name, health, attack, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.speed = speed
    
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
    def __init__(self, name, health, attack, speed, skill): # 생성자 오버라이딩
        super().__init__(name, health, attack, speed) # super로 부모클래스 호출
        
    def background(self):
        background = '하늘'
        print(f'{self.name}의 서식지: {background}')
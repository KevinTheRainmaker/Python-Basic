# 상속의 개념: 부모 클래스의 속성과 메서드를 자식 클래스가 가져오는 것

# 12-3 class + name 속성 & 배경을 보여주기 위한 background 메서드 추가
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
        # health에 따라 공격력이 변동
        # 최대 기본 공격력은 자체 공격력과 자체 스피드의 합산을 넘지 않음
        attack_point = self.attack * self.speed
        rage_point = attack_point // self.health

        basic_attack = (attack_point + rage_point) % (self.attack + self.speed)
        
        if basic_attack == 0:
            basic_attack = self.attack

        print(f'{self.name}의 기본공격! - {basic_attack}')
    
    def background(self):
        background = '땅'
        print(f'{self.name}의 서식지: {background}')

# 자식클래스 정의
class Warewolf(Monster): # Monster의 속성과 메서드를 상속 받음
    # 상속받았으므로 __init__ 생성자 생략 가능
    pass

class Shark(Monster):
    def background(self): # 메서드 재정의 (오버라이딩)
        background = '바다'
        print(f'{self.name}의 서식지: {background}')

class Dragon(Monster):
    def background(self):
        background = '하늘'
        print(f'{self.name}의 서식지: {background}')

warewolf = Warewolf('웨어울프', 2100, 800, 1100)
warewolf.background()

shark = Shark('샤크', 3000, 1000, 2000)
shark.background()

dragon = Dragon('드래곤', 10000, 4200, 2700)
dragon.background()
# 은행업무 토이 함수 - 전달값, 반환값 / 튜플 형태 반환 / 변수 업데이트
def open_account():
    print("새로운 계좌가 생성되었습니다.")
    return 0

def deposit(balance, money): # 전달값(input parameter) 두 개
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance+money))
    return balance+money # 반환값

def withdraw(balance, money):
    if balance>=money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance-money))
        return balance - money
    else:
        print("잔액이 부족합니다. 현재 잔액: {0}원".format(balance))
        return balance # if문에 각각 return값 부여 가능

def withdraw_night(balance, money): # 밤에 출금 - 수수료 부과
    commission = 100
    if balance>=money:
        print("[수수료 {0}원] 출금이 완료되었습니다. 잔액은 {1}원 입니다."\
            .format(commission, balance-money-commission)) # 줄바꿈
        return commission, balance - money - commission # 튜플 형태로 반환
    else:
        print("[수수료 {0}원] 잔액이 부족합니다. 현재 잔액: {1}원".format(commission, balance))
        return commission, balance

balance = open_account()
print(f"현재 잔액: {balance}원\n")

balance = deposit(balance, 5000) # 500-원 입금
balance = withdraw(balance, 2000) # 2000원 출금
commission, balance = withdraw_night(balance, 1000) # 1000원 출금 - 수수료 100원 & 튜플 형태의 반환값을 commission과 balance에 언패킹
print("\n최종 잔액: {0}원".format(balance))

print("\n")

# 기본값
def profile(name, age=21, main_lang="Python"):
    print("Name: {0}\tAge: {1}\tMain Language: {2}".format(name, age, main_lang))

profile("Alice") # age와 main_lang을 전달하지 않을 경우, 자동으로 age = 21, main_lang = "Python"으로 간주
profile("Brian",23) # age가 전달값에 의해 수정됨
profile("Chris", main_lang = "Java") # 건너뛰어 전달 시 키워드 값 명시
profile(main_lang="C", age = 22, name = "Daniel") # 키워드 값 사용 시 전달값의 순서 변경해도 정상적으로 들어감 

print("\n")

# 가변인자
def educate(name, age, *languages): # 가변인자 *languages
    print(f"{name} is {age} years old, and he(she) can use", end = " ") # default값 \n 대신 end 값 설정 가능
    for lang in languages:
        print(lang, end =" ")
    print() # 줄바꿈 위한 print문

educate("Erick", 25, "C", "C++", "C#", "Java", "Kotlin")
educate("Fredy", 21, "Python", "C", "JS")

print("\n")

# 지역변수 & 전역변수
gun = 10

def check_1(soldiers): # 경계근무 나가는 군인들
    gun = 20 # 지역변수로, 밖에 있는 전역변수 gun과는 이름만 같을뿐 다른 변수이다
    gun = gun - soldiers
    print("함수 내부에 남은 총 개수: {0}개".format(gun))

print(f"전체 총 개수: {gun}") 
check_1(2) # 2명이 경계근무 나감
print(f"남은 총 개수: {gun}")

print("\n")

def check_2(soldiers): # 전역변수를 함수 내부에서 사용
    global gun
    gun = gun - soldiers
    print("함수 내부에 남은 총 개수: {0}개".format(gun))

print(f"전체 총 개수: {gun}") 
check_2(3) # 3명이 경계근무 나감
print(f"남은 총 개수: {gun}")

# 전역변수를 과도하게 사용할 경우 코드 관리가 어려워지는 등의 문제가 있어 권장되는 방법은 아니다

print("\n")

gun = 10

def check_3(gun, soldiers): # gun을 변수로 받아서 사용
    gun = gun - soldiers
    print("함수 내부에 남은 총 개수: {0}개".format(gun))
    return gun # 외부로 반환

print(f"전체 총 개수: {gun}") 
gun = check_3(gun,4) # 4명이 경계근무 나감 - gun 업데이트
print(f"남은 총 개수: {gun}")
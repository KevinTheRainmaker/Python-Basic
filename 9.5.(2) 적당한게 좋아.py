# 50개의 의뢰 중 소요시간이 10일~25일인 의뢰만 받으려한다
# 의뢰는 5일에서 50일 사이의 난수이다

from random import *

def goodMiddle():
    # tasks = int(sample(range(5,51), 50)) -> 주의) sample은 범위 내에서 중복 없이 뽑는 것
        # 따라서 범위보다 큰 개수는 뽑지 못함
    tasks = []
    for i in range(50):
        tasks.append(randint(1,50))
    index = 1
    accept = 0

    for task in tasks:
        print(f"Task No.{index}, Estimated time required: {task}")
        index += 1
        if 10 <= task <= 25:
            print("Your task is accepted.")
            accept += 1
        else:
            print("Sorry. I don't want your task.")

    return f"Number of Customers I accept today: {accept}"

print(goodMiddle())
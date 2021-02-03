# for
for waiting in [0,1,2,3,4]: #range(5)
    print("No.{0}".format(waiting))

customers = ["Alice", "Brian", "Chris", "Daniel"]
for customer in customers:
    print("Here's the menu you ordered, {0}".format(customer))

# 파일이름에 /가 들어갈 경우 자동으로 폴더가 생성되어 들어간다.

# while
index = 3
while index >= 1:
    print("Here's the menu you ordered, {0}. I'll call you {1} more time(s).".format("Alice", index))
    index -= 1
    if index == 0:
        print("Your menu will be discarded. Sorry.")


# 무한루프
# time = 1
# while True:
#     print("Here's the menu you ordered, {0}. {1}".format("Brian", time))
#     time += 1


# continue & break
students = list(range(1,11))
absent = [2,5]
no_book = [7]
for student in students:
    if student in absent:
        continue # 아래를 더 이상 실행시키지 않고 다시 위로 돌아감
    elif student in no_book:
        print(f"Today's class is over. {student}, Follow me to the teacher's office.")
        break # 반복문 종료 및 탈출
    print(f"{student}, Come out and solve this problem.")


# 한 줄 for
print(students)
students = [i+100 for i in students]
print(students)

students = ["Alice", "Brian", "Chris", "Daniel", "Erick"]
students = [len(i) for i in students]
print(students)

students = ["Alice", "Brian", "Chris", "Daniel", "Erick"]
students = [i.upper() for i in students]
print(students)
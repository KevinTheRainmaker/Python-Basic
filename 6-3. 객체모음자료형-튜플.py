# 튜플 ()
menu = ("Cutlet", "Pasta")
print(menu[0])
print(menu[1])

# menu.add("Pizza")
# 튜플은 값의 추가 혹은 변경이 불가!

(name, age, language) = ("고강빈", 23, "Python") # 한 번에 여러 변수에 값 대입 가능

# 언패킹
person = ("홍길동", 20, 170, 70)
print('Name: %s, Age: %d, Height: %d, Weight: %d' % person)

name, age, height, weight = person
print('Name: %s, Age: %d, Height: %d, Weight: %d' % (name, age, height, weight))

persons = [person, ('Alice', 21, 160, 45), ('Brian', 24, 180, 75)]
for name, age, height, weight in persons:
    print('Name: %s, Age: %d, Height: %d, Weight: %d' % (name, age, height, weight))

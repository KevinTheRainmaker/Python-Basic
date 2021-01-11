# 리스트 []
alpha = ['a','b','c']

#위치 찾기
print(alpha.index('b'))

#추가: append(x)
alpha.append('d')
print(alpha)

#삽입: insert(index, x)
alpha.insert(1, "a-2")
print(alpha)

# 맨 뒤부터 꺼내기: pop()
D = alpha.pop()
print(alpha, D) #원본 수정

C = alpha.pop()
print(alpha, C)

B = alpha.pop()
print(alpha, B)

#같은 값 개수 세기: count(x)
alpha.append('a')
print(alpha, alpha.count('a')) 

#정렬: sort()
num = [5,3,2,4,1]
print(num)
print(num.sort()) #None 출력
print(num)

#뒤집기: reverse() - 주의) 정렬이 아닌 단순 뒤집기
num2 = [9,6,8,0,7]
print(num2)
num2.reverse()
print(num2)

#역정렬: sort(reverse=True)
num2.sort(reverse=True)
print(num2)

#지우기: clear()
print(num)
num.clear()
print(num)

#다양한 자료형 함께 사용
mix_list = ['고강빈', 1, True]
print(mix_list)
#mix_list.sort() - str과 int 사이에는 크기비교 불가능하므로 정렬 불가

####################################################################################################################

# 딕셔너리 {}
cabinet = {1:"Alice", 2:"Brian", 3:"Chris", 4:"David", 100:"Zeppelin"} #Key의 형태는 숫자형이든 문자형이든 상관 X
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3)) # == print(cabinet[3])
# print(cabinet[5]) - KeyError: 5 // 코드 종료
# print(cabinet.get(5)) - None 출력 이후 코드 지속
print(cabinet.get(5, "Erick")) # 5에 임시로 값 삽입
print(cabinet) # 원본 딕셔너리는 변동 X

print(3 in cabinet) #True
print(5 in cabinet) #False

#추가
print(cabinet)
cabinet[5] = "Erick"
print(cabinet)

#삭제: del
del cabinet[3]
print(cabinet)

#key만 출력: keys()
print(cabinet.keys()) # dict_keys([1, 2, 4, 100, 5])

#value만 출력: values()
print(cabinet.values()) # dict_values(['Alice', 'Brian', 'David', 'Zeppelin', 'Erick'])

#key, value 쌍으로 출력: items()
print(cabinet.items()) # dict_items([(1, 'Alice'), (2, 'Brian'), (4, 'David'), (100, 'Zeppelin'), (5, 'Erick')])

#비우기: clear()
cabinet.clear()
print(cabinet)

####################################################################################################################

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

####################################################################################################################

# 세트 {} - dict. 와 비슷하지만, 중복 불가, 순서 존재 X라는 차이점이 있다
my_set = {1,2,3,3,2,3,1}
print(my_set) # {1,2,3} 출력

jave = {'Alice', 'Brian', 'David'}
python = set(['Alice', 'Zeppelin', 'Erick']) # 둘 모두 set을 정의하는 방법
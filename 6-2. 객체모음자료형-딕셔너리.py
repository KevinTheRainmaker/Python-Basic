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
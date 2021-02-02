# 세트 {} - dict. 와 비슷하지만, 중복 불가, 순서 존재 X라는 차이점이 있다
my_set = {1,2,3,3,2,3,1}
print(my_set) # {1,2,3} 출력

java = {'Alice', 'Brian', 'David'}
python = set(['Alice', 'Zeppelin', 'Erick']) # 둘 모두 set을 정의하는 방법

# 교집합
print(java & python) # Alice 출력
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# 추가
python.add('Fedrick')
print(python)

# 삭제
java.remove('Brian')
print(java)
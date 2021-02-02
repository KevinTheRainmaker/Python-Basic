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
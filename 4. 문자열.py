s1 = "제 이름은 고강빈입니다"
print(s1)

s2 = "파이썬은 재밌습니다"
print(s2)

s3 = '''
제 이름은 고강빈이고,
GIST 학생입니다.
'''
print(s3)

#슬라이싱
civil_num = '991117-1234567'

print('성별: '+civil_num[7]) #index7(8번째)값 출력
print('생년월일: '+civil_num[:6]) #index6(7번째)이전까지 출력
print('생일: '+civil_num[2:6]) #index2부터 index6 이전까지 출력
print('뒤 7자리: '+civil_num[7:]) # print('뒤 7자리: '+civil_num[-7:])

#문자열 처리함수
python = "Pyton is Amazing!"
print(python.lower()) #전부 소문자로
print(python.upper()) #전부 대문자로

print(python[0].isupper()) #index0이 대문자인지 확인
print(len(python)) #길이

print(python.replace('Pyton', 'Java')) #앞의 문자열을 뒤의 문자열로 대체

index = python.index('n')
print(index) #'n'의 첫번째 위치의 index 출력
index = python.index('n',index+1) #앞에서의 index 위치보다 한 칸 뒤에서부터 시작하여 index 업데이트
print(index)

print(python.find('n')) #python.index('n')와 비슷하지만 찾는 값이 없을 시 -1 반환 (index는 오류발생)

print(python.count('n')) #'n'의 개수 세기


#문자열 포맷팅

#방법1
print("나는 %d살입니다" %23)
print("나는 %s을 좋아해요" %"파이썬")
print("Apple은 %c로 시작해요" %"A")
print("나는 %s색과 %s색을 좋아해요" %("빨간", "파란")) # 순서대로 삽입

#방법2
print("나는 {}살입니다".format(23))
print("나는 {}을 좋아해요".format("파이썬"))
print("Apple은 {}로 시작해요".format("A"))
print("나는 {}색과 {}색을 좋아해요".format("빨간", "파란")) # 순서대로 삽입
print("나는 {0}색과 {1}색을 좋아해요".format("빨간", "파란")) # 순서대로 삽입
print("나는 {1}색과 {0}색을 좋아해요".format("빨간", "파란")) # 순서 바꿔서 삽입

#방법3
print("나는 {age}살이고 {color}색을 좋아해요".format(age = 23, color = "파란")) # {}안의 변수에 맞게 삽입
print("나는 {color}색을 좋아하고 {age}살이에요".format(age = 23, color = "파란")) # {}안의 변수에 맞게 삽입

#방법4 (v3.6 이상)
age = 23
color = "파란"
print(f"나는 {age}살이고 {color}색을 좋아해요") # {}안의 변수에 맞게 삽입


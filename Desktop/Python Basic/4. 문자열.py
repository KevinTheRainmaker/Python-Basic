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

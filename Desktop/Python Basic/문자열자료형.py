#간단한 문자열 출력
print('풍선') # ''로 출력가능
print("나비") # ""로 출력가능
print('ㅋ'*9) # 문자열 연산 가능


#Boolean 자료형
print(5 > 10) #5는 10보다 작으므로 False 출력
print(5 < 10) #5는 10보다 작으므로 True 출력
print(1+2==3) #1+2=3이므로 True 출력
print(1 != 3) #1은 3과 같지않으므로 True출력

print((3>0)and(2<10)) #모두 참이므로 True 출력
#print((3>0)&(2<10))

print((3>0) or (3>5)) #둘 중 하나만 참이어도 True 출력
#print((3>0)|(3>5))

print(10>3>5) #False 출력

print(True)
print(not True) #False 출력
print(not(5 < 10)) #5는 10보다 작으므로 True => not에 의해 False 출력 


#문자열 변수
animal = "강아지"
name = "초코"
age = 4
hobby = "산책"
is_adult = age>=3

print("우리집"+animal+"의 이름은"+name+"입니다.")
'''
print("우리집",animal,"의 이름은",name,"입니다.")
    띄어쓰기되어 결합됨
''' #여러 줄 주석
#ctrl + K + F
 
print("%s의 나이는 %d이고, %s을 좋아합니다",name,age,hobby)
print("%s는 어른인가요? ")
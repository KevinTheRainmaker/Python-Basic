#\n : 줄바꿈
print("가나다\n라마바\n사아자")
    # print문의 end의 기본값은 \n이다
print("I love", end = " ")
print("Python")

#\", \' : 문장 내 따옴표  
print("저는 'GIST' 학생입니다")
print('저는 "GIST" 학생입니다')
print("저는 \"GIST\" 학생입니다")

# \\ : 문장 내 \
print("C:\\Users\\kgbko\\Desktop") #C:\Users\kgbko\Desktop 

#\r : 커서를 맨 앞으로 이동
print("Black King\rWhite")

#\b : 한 글자 삭제
print("Blackk\b King")
    #응용
import time
print("Loading.", end = "\b")
time.sleep(1)
print("..", end ="\b")
time.sleep(1)
print("..")

#\t : tab
print("Jumping\tRabbit")



#Practice : 메일 주소 입력 시 아이디와 도메인 분리 후 아이디와 도메인을 한 글자씩 번갈아서 출력
email = input("Enter your email: ")

id = email.split("@")[0]
domain = email.split("@")[1]
print(id,"/", domain)
print(len(id),"/",len(domain))

i=0
result = ""
while i//2 < max(len(id), len(domain)):
    if i%2 == 0:
        letter = str(id[i//2])
        i= i+1
    else:
        letter = str(domain[i//2])
        i= i+1
    result += letter

print(result)
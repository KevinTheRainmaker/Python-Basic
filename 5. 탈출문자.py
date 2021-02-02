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
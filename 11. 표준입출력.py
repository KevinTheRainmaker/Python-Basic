import sys
# print('Python', 'Java', 'C', file = sys.stdout) # 표(준 출력
# # print('Python', 'Java', 'C', file = sys.stderr) # 표준 에러 - 로그 처리를 하면 둘이 다르게 로깅됨

# scores = {'Math': 10, 'English': 50, 'Python': 100}

# for subject, score in scores.items(): # item이 아니라 items임에 주의
#     print(subject, score)

# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep = ' : ') # 왼쪽/오른쪽 정렬 - ()칸 확보, int형 object에는 rjust attribute가 존재하지 않는다.


# for num in range(1,11):
#     print('대기번호 : ' +str(num).zfill(3)) # 001 형태의 format으로 만들어줌, 이 경우에도 int형 object에는 정상적으로 적용되지 않음
 
# answer = input()
# print(answer, type(answer)) # 입력값에 상관없이 항상 str로 받음 -> int(intput())

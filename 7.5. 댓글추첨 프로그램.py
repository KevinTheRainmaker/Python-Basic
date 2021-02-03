# 댓글 작성자 중 4명을 선정하여 1명은 치킨, 3명은 커피 쿠폰을 주는 코드

# 1부터 20까지의 아이디를 가진 20명의 사람이 댓글을 작성하였다고 가정
# 무작위 추첨 / 중복불가

from random import *
present = []
temp = []
def gift():
    for i in range(4):
        present.append(randint(1,20))
    print("\n\t---당첨자 발표---\n")
    print(f"\t치킨 당첨자: {present[0]}번\n")
    for j in range(1,4):
        temp.append(present[j])
        temp.sort()
        print(f"\t커피 당첨자: {temp[j-1]}번")
    
    print("\n\t-----------------\n")

gift()
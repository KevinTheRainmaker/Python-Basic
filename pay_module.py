# 모듈 사용이유: 프로그램 기능별로 파일을 나눠서 유지보수 등 관리를 편하게 하고자
# 모듈: 한 개의 완성된 프로그램 파일

# Example: 결제 정보, 관리 모듈

# 변수
version = 1.0

# 함수
def printAuthor():
    print('Start Coding')

# 클래스
class Pay:
    def __init__(self, id, price, time):
        self.id = id
        self.price = price
        self.time = time
    
    def get_pay_info(self):
        return f'{self.time}\n{self.id}\n{self.price}'

# 해당 파일을 직접 실행했을때만 실행: 모듈로 불러와서 실행 시 실행 X
if __name__ == '__main__':
    print('pay 모듈 실행')
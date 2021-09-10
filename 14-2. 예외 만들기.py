# raise로 에러 만들기
try:
    num = int(input('음수를 입력해주세요: '))
    if num >= 0:
        raise Exception('양수를 입력하셨습니다.')
except Exception as e:
    print('에러발생', e)

# 에러 만들기
'''
class exceptionName(Exception):
    def __init__(self):
        super().__init__('에러 메시지')
'''

class PositiveNumError(Exception):
    def __init__(self):
        super().__init__('양수를 입력하셨습니다.')

try:
    num = int(input('음수를 입력해주세요: '))
    if num >= 0:
        raise PositiveNumError
except PositiveNumError as e:
    print('에러발생', e)

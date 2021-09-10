'''
try:
    예외가 발생할 수 있는 코드
except:
    예외 발생 시 처리할 코드
else:
    예외 발생하지 않을 경우 실행할 코드
finally:
    예외 발생 여부에 관계없이 항상 실행되는 코드 # 리소스 반환을 위해 주로 사용됨
'''

# 예제: 원화와 환율을 입력받고 이를 달러로 변환하는 프로그램
won = input('원화 금액을 입력하세요: ')
dollar = input('환율을 입력하세요: ')
try:
    print(int(won)/int(dollar))
except ValueError as e:
    print('문자열 예외 발생', e)
except ZeroDivisionError as e:
    print('0으로 나눌 수 없습니다.', e)
else:
    print('에러가 발생하지 않고 성공적으로 처리되었습니다.')
finally: # 파일 닫기: 리소스 반환
    print('상상 실행되는 코드')
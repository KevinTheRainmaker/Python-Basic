# try-except
try:
    1/0
    print('Run Successfully')
except ZeroDivisionError as e:
    print(type(e))
    print(e)

# try-except-finally
# finally는 에러 여부와 관계 없이 무조건 실행되는 영역
try:
    1/1
    print('Run Successfully')
except ZeroDivisionError as e:
    print(type(e))
    print(e)
finally:
    print('Process End.')
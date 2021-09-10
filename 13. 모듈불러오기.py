import pay_module

# 변수 사용
print(pay_module.version)

# 함수 사용
pay_module.printAuthor() # 실행 시 __pycache__ 내에 pyc 파일이 생성됨: 빠른 실행을 위한 컴파일된 파일

# 클래스 사용
pay_info = pay_module.Pay('A120382', 13000, '2021-09-10')
print(pay_info.get_pay_info())
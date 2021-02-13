# 다음 공식에 따라 표준 체중을 구하는 프로그램을 작성하자

# 남자: 키(m) x 키(m) x 22
# 여자:  키(m) x 키(m) x 21

# 조건1: 표준 체중은 별도 함수 내에서 계산
# 조건2: 표준 체중은 소수점 둘째 자리까지 표시

def std_weight(sex, height):
    if sex == "남자":
        return height * height * 22
    else:
        return height * height * 21


height = 172
sex = "남자"
std = round(std_weight(sex, height/100), 2) # 소수점 둘째 자리까지 표기 (셋째 자리에서 반올림)

print("키 {0}cm의 {1}의 표준 체중은 {2}kg입니다.".format(height, sex, std))
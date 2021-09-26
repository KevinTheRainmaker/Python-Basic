# re 모듈의 메서드
'''
종류 / 기능 / 있는 경우 / 없는 경우
match / 문자열을 처음부터 검색 / match obhect 1개 / None
search / 문자열 전체를 검색 / match obhect 1개 / None
findall / 문자열 전체를 검색 / 문자열 리스트 / 빈 리스트
finditer / 문자열 전체를 검색 / match object iterator / None
fullmatch / 패턴과 문자열이 남는 부분 없이 완벽하게 일치 / match object 1개 / None
'''

# match object의 메서드
'''
종류 / 반환 / 예
group / 매칭된 문자열 반환 / people
start / 매칭된 문자열의 시작 위치 / 5
end / 매칭된 문자열의 끝 위치 / 11
span / 매칭된 문자열의 (시작,끝) 튜플 / (5,11)
'''
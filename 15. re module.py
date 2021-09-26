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

import re

# 1. re module의 메서드
str = 'love your people, love your work, love yourself'

'''
1) match
    re.match('패턴', 찾고자 하는 문자열)
'''
result = re.match('love', str)
print(result)
# <re.Match object; span=(0, 4), match='love'>

result = re.match('your', str)
print(result)
# None

'''
2) search
    re.search('패턴', 찾고자 하는 문자열)
'''
result = re.search('love', str)
print(result)
# <re.Match object; span=(0, 4), match='love'>

result = re.search('your', str)
print(result)
# <re.Match object; span=(5, 9), match='your'>

'''
3) findall
    re.findall('패턴', 찾고자 하는 문자열)
'''
results = re.findall('love', str)
print(results)
# ['love', 'love', 'love']

'''
4) finditer
    re.finditer('패턴', 찾고자 하는 문자열)
'''
results = re.finditer('love', str)
print(results)
# <callable_iterator object at 0x1007c0fa0>

'''
5) fullmatch
    re.fullmatch('패턴', 찾고자 하는 문자열)
'''
str2 = 'Boys be ambitious'
result1 = re.fullmatch('Boys be ambitious', str2)
result2 = re.fullmatch('Boys be ambitious!', str2)
result3 = re.fullmatch('.*', str2) # 정규표헌식

print(result1)
# <re.Match object; span=(0, 17), match='Boys be ambitious'>

print(result2)
# None

print(result3)
# <re.Match object; span=(0, 17), match='Boys be ambitious'>
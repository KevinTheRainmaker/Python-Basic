#Practice : 메일 주소 입력 시 아이디와 도메인 분리 후 아이디와 도메인을 한 글자씩 번갈아서 출력
email = input("Enter your email: ")

id = email.split("@")[0]
domain = email.split("@")[1]
print(id,"/", domain)
print(len(id),"/",len(domain))

i=0
result = ""
while i//2 < max(len(id), len(domain)):
    if i%2 == 0:
        letter = str(id[i//2])
        i= i+1
    else:
        letter = str(domain[i//2])
        i= i+1
    result += letter

print(result)
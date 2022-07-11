# 1157
# 입력받은 영어를 전부 대문자로 바꾼후에 아스키 코드에 따른 알파벳 개수를 구한다.
count = 0
input_str = input()

input_str = input_str.upper()
alp = [0 for i in range(26)]

for i in input_str:
    alp[ord(i)%65] += 1

for i in alp:
    if i == max(alp):
        count += 1

if count == 1:
    print(chr(alp.index(max(alp))+65))
else:
    print("?")

'''
입력
Mississipi
출력
?
'''
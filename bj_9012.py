# 9012
# 열린 괄호는 +로, 닫힌 괄호는 -로 전체 합에 따른 올바른 괄호 문자열 여부를 확인한다.
def count_check(vps):
    sum = 0
    for i in range(len(vps)):
        for f in vps[i]:
            if f == chr(40):
                sum += 1
            elif f == chr(41):
                sum -= 1

            if sum < 0:
                return 'NO'
                break
    if sum == 0 :
        return 'YES'
    else:
        return 'NO'

vps = []
check = []

n = int(input())

for i in range(n):
    vps.append(input())

for i in vps:
    print(count_check(i))
'''
입력
5
1 2
1 5
3 5
4 5
4
1
3
2
5
출력
7
'''
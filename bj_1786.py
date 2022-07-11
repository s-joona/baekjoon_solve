# 1786

T = input()
P = input()
n = len(T)
m = len(P)
k = 0
locate = []

check_str = [0 for i in range(len(P))]

for i in range(1, m):
    while k > 0 and P[k] != P[i]:
        k = check_str[k-1]

    if P[i] == P[k]:
        k += 1
        check_str[i] = k

k = 0
count = 0

for i in range(n):
    while k > 0 and T[i] != P[k]:
        k = check_str[k-1]
    if T[i] == P[k]:
        if k == (m-1):
            count += 1
            locate.append(i-m+2)
            k = check_str[k]
        else:
            k += 1

print(count)
print(*locate)
'''
입력
ABC ABCDAB ABCDABCDABDE
ABCDABD
출력
1
16
'''
#14681
# x와 y를 0을 기준으로 크고 작음에 따라 해당하는 사분면 출력하기

x = int(input())
y = int(input())
result = 0
if x > 0 :
    if y > 0:
        result = 1
    else :
        result = 4

else :
    if y > 0 :
        result = 2
    else :
        result = 3

print(result)

'''
입력 : 12 5
출력 : 1

입력 : 9 -13
출력 : 4
'''
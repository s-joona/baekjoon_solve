# 11729
# 하노이탑 : 재귀함수를 사용한다.
def hanoi(n, from_t, to_t):
    if n == 1:
        print(from_t, to_t)
        return

    hanoi(n-1, from_t, 6-from_t-to_t)
    print(from_t, to_t)
    hanoi(n-1,6-from_t-to_t,to_t)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3)

'''
입력 3
출력
7
1 3
1 2
3 2
1 3
2 1
2 3
1 3
'''
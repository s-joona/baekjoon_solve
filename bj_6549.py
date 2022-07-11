# 6549
# 높이에 따른 리스트를 생성해 조건에 맞으면 스택에 넣고, 아니면 스택에서 제거하는 방식을 사용한다.
import sys

while True:
    result = 0
    stack = [(0, 0)]

    h = list(map(int, sys.stdin.readline().split()))
    n = h.pop(0)
    h.append(0)

    if n == 0: break

    for i in range(n + 1):
        idx = i
        while h[i] < stack[-1][-1]:
            idx, height = stack.pop()
            result = max(result, (i - idx) * height)
        stack.append((idx, h[i]))

    print(result)

'''
입력
7 2 1 4 5 1 3 3
4 1000 1000 1000 1000
0
출력
8
4000
'''
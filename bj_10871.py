# 10871
# list에 x보다 작은 값들만 출력한다.
N, X = map(int, input().split())
n_list = list(map(int, input().split()))

for i in range(N):
    if n_list[i] < X :
        print(n_list[i], end = ' ')
'''
입력
10 5
1 10 4 9 2 3 8 5 7 6
출력
1 4 2 3
'''

# 1546
# 입력받은 점수 / 최고점 * 100을 계산한 새로운 리스트를 만들어서 평균을 구한다.
N = int(input())
score = list(map(int, input().split()))
max_score = max(score)

fix_score = [score[i]/max_score*100 for i in range(N) ]

print(sum(fix_score)/N)

'''
입력
3
40 80 60
출력
75.0
'''
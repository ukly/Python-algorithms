import sys
input = sys.stdin.readline

n = int(input())
sizes = []
ranks = []

for i in range(n):
    x, y = map(int, input().split())  
    sizes.append((x, y))              # 몸무게, 키를 리스트 안에 튜플로 저장

for i in range(n):
    rank = 1                                                        #순위 기본값으로 1지정
    for j in range(n):
        if sizes[i][0] < sizes[j][0] and sizes[i][1] < sizes[j][1]:   #자신을 포함한 모든 사람과 비교하여 사이즈가 더 큰 사람이 있으면 순위를 1 낮춤
            rank += 1
    ranks.append(rank)

for r in ranks:
    print(r, end=' ')

import sys
input = sys.stdin.readline

n = int(input())                           
times = list(map(int, input().split()))
res = 0

times.sort()           #걸리는 시간의 최소 순으로 정렬

for i in range(n):
    res += sum(times[:i+1])  #계산할 사람 + 그 앞순서의 사람들 값의 합

print(res)

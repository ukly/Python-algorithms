import heapq
import sys
input = sys.stdin.readline

N = int(input())

dasom = int(input())
candidates = []

for _ in range(N - 1):                  #후보들을 최대힙으로 관리
    x = int(input())
    heapq.heappush(candidates, (-x, x))

ct = 0
while candidates:                       #후보들의 표가 다 빠지면 자동으로 끝
    max_candidate = heapq.heappop(candidates)
    if dasom > max_candidate[1]:        #다솜이의 표가 후보들 중 최대값보다 많아질 경우 끝
        break
    reduced_candidate = (max_candidate[0] + 1, max_candidate[1] - 1)
    heapq.heappush(candidates, reduced_candidate)
    dasom += 1
    ct += 1
    
print(ct)

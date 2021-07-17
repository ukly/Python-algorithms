import heapq
import sys
input = sys.stdin.readline

n = int(input())

presents = []

for i in range(n):
    ip = list(map(int, input().split()))
    
    a = ip[0]   #a값을 입력값 중 첫번째
    
    if a == 0:  #a가 0이면 선물을 출력하거나 -1을 출력
        if presents:
            print(heapq.heappop(presents)[1])
        else:
            print(-1)
    else:       #a가 0이 아니면 새로운 선물들 충전
        for i in range(1, len(ip)):
            heapq.heappush(presents, (-(ip[i]), ip[i]))
    

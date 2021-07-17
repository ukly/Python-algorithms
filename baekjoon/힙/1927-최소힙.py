import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
heapq.heapify(heap)
for i in range(N):
    num = int(input())
    if num == 0:
        try:                            #heap이 비어있는 경우에는 0을 
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, num)

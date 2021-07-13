import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
heapq.heapify(heap)
for i in range(N):
    num = int(input())
    if num == 0:
        try:
            print(heapq.heappop(heap) * -1)
        except:
            print(0)
    else:
        heapq.heappush(heap, num * -1)

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
            print(heapq.heappop(heap) * -1) #최대힙은 최소힙에 -1을 곱해주고 다시 빼낼때 -1을 곱해주고 빼내는 방식
        except:
            print(0)
    else:
        heapq.heappush(heap, num * -1)

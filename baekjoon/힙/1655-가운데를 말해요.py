import heapq
import sys
input = sys.stdin.readline

N = int(input())
min_heap, max_heap = [], []
for i in range(N):
    x = int(input())
    if len(min_heap) == len(max_heap):
        heapq.heappush(min_heap, (-x, x))           #최대힙을 구현할때 튜플로 구현 (최소힙도 동일하게)
    else:
        heapq.heappush(max_heap, (x, x))
    if max_heap and min_heap[0][1] > max_heap[0][1]:            
        min_num, max_num = heapq.heappop(min_heap)[1], heapq.heappop(max_heap)[1]
        heapq.heappush(min_heap, (-max_num, max_num))
        heapq.heappush(max_heap, (min_num, min_num))
    a = min_heap[0][1]
    print(a)
    
   

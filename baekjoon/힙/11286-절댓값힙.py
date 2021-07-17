import heapq
import sys
input = sys.stdin.readline

min_heap, max_heap = [], []

heapq.heapify(min_heap)
heapq.heapify(max_heap)

N = int(input())

for i in range(N):
    x = int(input())
    if x == 0:
        if min_heap and max_heap:                 #음수 양수 둘다 있는 경우
            min_num = heapq.heappop(min_heap)
            max_num = heapq.heappop(max_heap)
            if min_num <= max_num:                #음수와 양수 중 각각 절댓값이 가장 작은수가 같으면 음수를 출력
                print(min_num * -1)
                heapq.heappush(max_heap, max_num)
            else:                                 #양수의 절댓값이 작으면 양수를 출력
                print(max_num)
                heapq.heappush(min_heap, min_num)
        elif min_heap:                            #음수만 있으면 음수 중 절댓값이 작은 수 출력
            print(heapq.heappop(min_heap) * -1)
        elif max_heap:                            #양수만 있으면 양수 중 절댓값이 작은 수 출력
            print(heapq.heappop(max_heap))
        else:                                     #둘 다 비어있으면 0 출력
            print(0)
            
    elif x < 0:
        heapq.heappush(min_heap, x * -1)
    else:
        heapq.heappush(max_heap, x)

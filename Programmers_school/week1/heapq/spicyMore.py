import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville) # 최솟값만을 반복해서 찾기 때문에 힙정렬을 통해 min heap을 만들어줌

    while scoville[0] < K: 
        if len(scoville) == 1:
            return -1
        new_food = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, new_food)
        answer += 1

    return answer

import heapq

def solution(no, works):
    result = 0
    
    works_reverse = []
    
    heapq.heapify(works_reverse)
    
    for work in works:                    #heap의 모든 아이템들에 -1을 곱해줌으로써 maxheap을 유사하게 구현
        works_reverse.append(work * -1)
        
    for i in range(no):
        min_work = heapq.heappop(works_reverse)
        if min_work:                                      #젤 적은 시간이 걸리는 일이 0일경우 더해주면 오히려 절댓값이 커지기 때문에 연산을 멈춰야함
            heapq.heappush(works_reverse, min_work + 1)
        else:
            return 0

    return sum([work*work for work in works_reverse])
    
    return result

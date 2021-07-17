import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

cards = list(map(int, input().split()))

heapq.heapify(cards)

for i in range(m):
    new_card = heapq.heappop(cards) + heapq.heappop(cards)  #카드들의 최솟값과 
    heapq.heappush(cards, new_card)
    heapq.heappush(cards, new_card)

print(sum(cards))

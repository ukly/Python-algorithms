import heapq
import sys
input = sys.stdin.readline

n = int(input())
answer = 0

cards = []
for i in range(n):
    card = int(input())
    heapq.heappush(cards, card)

for j in range(n-1):
    new_card = heapq.heappop(cards) + heapq.heappop(cards)    #카드를 합치는 횟수는 동일하지만 최소로 하기 위해서는 적은 
    answer += new_card
    heapq.heappush(cards, new_card)
    
print(answer)

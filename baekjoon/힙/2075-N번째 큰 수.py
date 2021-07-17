import heapq
import sys
input = sys.stdin.readline

n = int(input())

nums = []
for i in range(n):
    for num in list(map(int, input().split())):
        heapq.heappush(nums, num)
    nums = heapq.nlargest(n, nums)        #필요한 N만큼만 추출하여 메모리 최소화
heapq.heapify(nums)
print(heapq.heappop(nums))

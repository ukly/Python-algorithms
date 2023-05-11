from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

elements = deque([element for element in range(1, n+1)])

answer = 0

for num in nums:
    count = 0
    while True:
        length = len(elements)
        element = elements.popleft()
        if element != num:
            elements.append(element)
            count += 1
        else:
            break
    if count > length//2:
        answer += length - count
    else:
        answer += count
        
print(answer)

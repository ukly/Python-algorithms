from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

elements = deque([element for element in range(1, n+1)])  1부터 n까지 담긴 덱

answer = 0

for num in nums:
    count = 0
    while True:
        length = len(elements)            
        element = elements.popleft()
        if element != num:                #1번 연산을 수행하여 popleft한 값이 원하는 값이 아니면
            elements.append(element)      #덱 맨 뒤에 추가
            count += 1                    #연산 횟수 기록
        else:
            break
    if count > length//2:                 #1번 연산을 덱 길이의 절반보다 많이했으면
        answer += length - count          #3번 연산보다 2번 연산을 통해 접근하는 것이 빠름
    else:                                 #반대의 경우
        answer += count                   #2번 연산보다 3번 연산을 통해 접근하는 것이 빠름
        
print(answer)

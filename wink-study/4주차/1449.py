import sys
from collections import deque

input = sys.stdin.readline

n, l = map(int, input().split())
holes = list(map(int, input().split()))
holes.sort()
cnt = 0

deq = deque(holes)         #구멍들을 덱으로 만들어줌

while(deq):
    hole = deq.popleft()        #뚫려있는 가장 왼쪽 구멍
    tapeRight = hole + (l-0.5)  #해당 구멍을 막을 수 있는 최대한 오른쪽의 위치에 붙일 수 있는 테이프
    cnt += 1                    #테이프 사용랑 추가
    while(deq):
        nextHole = deq.popleft()           #그다음 구멍
        if (nextHole + 0.5 > tapeRight):   #이전에 붙였던 테이프가 덮는 범위에 들어가는지 체크
            deq.appendleft(nextHole)       #만약 이전에 붙였던 테이프에 닿지 않으면 다시 덱에 추가하고 while문 끝냄
            break;

print(cnt)

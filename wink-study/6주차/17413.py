import sys
from collections import deque
input = sys.stdin.readline

string = input().rstrip()

string = deque(list(string))
stack = list()                              # 스택에는 <> 밖의 문자열을 저장
deq = deque()                               # 덱에는 <>안의 문자열을 저장

while string:
    char = string.popleft()
    if char == '<':                          # '<'을 만나면 
        while(deq):                          # 이전에 만들어진 문자열을 출력
            print(deq.popleft(), end='')
        while(stack):
            print(stack.pop(), end='')

        deq.append(char)
        while(char != '>'):                  # '>'을 만날때 까지 덱에 추가
            char = string.popleft()
            deq.append(char)
    elif char == ' ':                        # ' '을 만나면
        while(deq):                          # 이전에 만들어진 문자열을 출력
            print(deq.popleft(), end='')
        while(stack):
            print(stack.pop(), end='')
        print(' ', end='')
    else:                                    # <> 밖의 문자열을 생성
        stack.append(char)

while(deq):                                  # 남은 문자열 출력
    print(deq.popleft(), end='')
while(stack):
    print(stack.pop(), end='')

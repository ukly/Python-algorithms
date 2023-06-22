import sys
from collections import deque
input = sys.stdin.readline

string = input().rstrip()

string = deque(list(string))
stack = list()
deq = deque()

while string:
    char = string.popleft()
    if char == '<':
        while(deq):
            print(deq.popleft(), end='')
        while(stack):
            print(stack.pop(), end='')

        deq.append(char)
        while(char != '>'):
            char = string.popleft()
            deq.append(char)
    elif char == ' ':
        while(deq):
            print(deq.popleft(), end='')
        while(stack):
            print(stack.pop(), end='')
        print(' ', end='')
    else:
        stack.append(char)

while(deq):
    print(deq.popleft(), end='')
while(stack):
    print(stack.pop(), end='')

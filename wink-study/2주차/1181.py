import sys
input = sys.stdin.readline
N =int(input())
str_list = []
for i in range(N):
    w = input()
    if w not in str_list:
        str_list.append(w)
str_list.sort()
str_list.sort(key=len)
for n in str_list:
    print(n, end='')

import sys
input = sys.stdin.readline
N =int(input())
str_list = []
for i in range(N):
    w = input()
    if w not in str_list:
        str_list.append(w)
str_list.sort()     #우선 사전순으로 정렬
str_list.sort(key=len)  #그 뒤에 길이순으로 정렬 해준다.
for n in str_list:
    print(n, end='')

import sys
input = sys.stdin.readline

s = set()

n = int(input())

for _ in range(n):
    opers = list(input().split())
    oper = opers[0]
    if len(opers) > 1:
        num = int(opers[1])
    if oper == "add":
        s.add(num)
        continue
    elif oper == "remove":
        s.discard(num)
        continue
    elif oper == "check":
        if num in s:
            print(1)
        else:
            print(0)
        continue
    elif oper == "toggle":
        if num in s:
            s.discard(num)
            continue
        else:
            s.add(num)
            continue
    elif oper == "all":
        s = set([n for n in range(1, 21)])
        continue
    elif oper == "empty":
        s = set()
        continue

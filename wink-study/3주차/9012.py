n = int(input())

for i in range(n):
    ps = input()
    count = 0
    for s in ps:
        if s == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            print("NO")
            break
    if count > 0:
        print("NO")
        continue
    elif count < 0:
        continue
    else:
        print("YES")

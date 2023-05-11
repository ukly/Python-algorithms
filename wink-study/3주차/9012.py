n = int(input())

for i in range(n):
    ps = input()
    count = 0
    for s in ps:
        if s == '(':                  #괄호 문자열은 소괄호로 일정하기 때문에 
            count += 1               
        else:
            count -= 1
        if count < 0:
            print("NO")               #count가 0보다 작아지거나
            break
    if count > 0:                     #모든 괄호를 거쳤는데 count가 0보다 크지(여는 괄호가 더 많음)않으면 된다.
        print("NO")
        continue
    elif count < 0:                   #이중 for문 출력을 위해 억지로 만든...
        continue
    else:
        print("YES")

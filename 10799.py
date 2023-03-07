brackets = input()

stack = []
last_bracket = ''
pieces = 0
pipes = 0

for bracket in brackets:
    if bracket == '(':
        stack.append(bracket)
    else:
        if stack[-1] == '(' and last_bracket == '(':    #레이저인 경우
            stack.pop()
            pieces += len(stack)
        elif stack[-1] == '(' and last_bracket == ')':   #쇠막대기의 끝인 경우
            stack.pop()
            pipes += 1
    last_bracket = bracket

result = pieces + pipes

print(result)


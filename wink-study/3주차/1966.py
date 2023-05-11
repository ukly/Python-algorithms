from collections import deque

testcases = int(input())

for i in range(testcases):
    n, k = map(int, input().split(" "))

    docs = list(map(int, input().split()))
    
    for i in range(n):
        docs[i] = (docs[i], i)    #(문서들의 중요도, 인덱스)로 구성되어 있는 투플
    
    docs_deq = deque(docs)    #리스트를 덱으로 변경
    
    count = 0
    op = -1  

    while op != k:
        if docs_deq[0][0] < max(docs_deq)[0]:  
            docs_deq.append(docs_deq.popleft())
        else:
            op = docs_deq.popleft()[1]
            count += 1
 
 

            
    print(count)

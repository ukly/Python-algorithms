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
        if docs_deq[0][0] < max(docs_deq)[0]:    #문서의 중요도가 최대값이 아니면
            docs_deq.append(docs_deq.popleft())  #문서를 덱의 맨 뒤로 넣어줌
        else:                                    #문서의 중요도가 젤 큰 문서가 앞으로 오면
            op = docs_deq.popleft()[1]           #문서의 중요도가 k인 문서가 나올때까지 popleft진행하며 count
            count += 1
 
 

            
    print(count)

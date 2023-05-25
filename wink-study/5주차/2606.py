import sys
input = sys.stdin.readline

n = int(input())
links = int(input())
infected = [1]                                    #감염된 컴퓨터들을 기록

nodesLink = [[i] for i in range(1, n+1)]      #노드의 링크 정보를 담을 리스트

def dfs(host ,l, infected):                       #host는 탐색을 하는 위치, l은 링크 정보를 담은 리스트, infected는 감염된 컴퓨터들을 기록
    nodes = l[host-1]                             
    for i in range(1, len(nodes))
        if nodes[i] not in infected:
            infected.append(nodes[i])
            infected = dfs(nodes[i], l, infected)
    return infected

for _ in range(links):
    x, y = map(int, input().split())
    nodesLink[x-1].append(y), nodesLink[y-1].append(x)

infected = dfs(1, nodesLink, infected)
print(len(infected)-1)

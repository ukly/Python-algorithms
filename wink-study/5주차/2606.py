import sys
input = sys.stdin.readline

nodes = int(input())
links = int(input())
infected = [1]

nodesLink = [[i] for i in range(1, nodes+1)]

def dfs(host ,l, infected):
    nodes = l[host-1]
    for i in range(1, len(nodes)):
        if nodes[i] not in infected:
            infected.append(nodes[i])
            infected = dfs(nodes[i], l, infected)
    return infected

for _ in range(links):
    x, y = map(int, input().split())
    nodesLink[x-1].append(y), nodesLink[y-1].append(x)

infected = dfs(1, nodesLink, infected)
print(len(infected)-1)

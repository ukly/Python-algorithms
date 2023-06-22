import sys
input = sys.stdin.readline

n = int(input())

rgbOfHouses = [[0, 0, 0]]


for i in range(1, n+1):
    r, g, b = map(int, input().split())
    costR = min(rgbOfHouses[i-1][1], rgbOfHouses[i-1][2]) + r
    costG = min(rgbOfHouses[i-1][0], rgbOfHouses[i-1][2]) + g
    costB = min(rgbOfHouses[i-1][0], rgbOfHouses[i-1][1]) + b
    rgbOfHouses.append([costR, costG, costB])

print(min(min(rgbOfHouses[n][0], rgbOfHouses[n][1]), rgbOfHouses[n][2]))

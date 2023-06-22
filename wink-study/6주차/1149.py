import sys
input = sys.stdin.readline

n = int(input())

rgbOfHouses = [[0, 0, 0]]


for i in range(1, n+1):
    r, g, b = map(int, input().split())
    costR = min(rgbOfHouses[i-1][1], rgbOfHouses[i-1][2]) + r   # i번째에 red를 선택했을 때의 cost
    costG = min(rgbOfHouses[i-1][0], rgbOfHouses[i-1][2]) + g   # i번째에 greend을 선택했을 때의 cost
    costB = min(rgbOfHouses[i-1][0], rgbOfHouses[i-1][1]) + b   # i번째에 b를 선택했을 때의 cost
    rgbOfHouses.append([costR, costG, costB])                   # i번째에 각 선택에 따른 cost를 저장

print(min(rgbOfHouses[n][0], rgbOfHouses[n][1], rgbOfHouses[n][2])) #가장 cost 누적이 작은 값을 선택

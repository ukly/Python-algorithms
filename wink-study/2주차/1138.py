import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
l = [0]                 // 주어진 인덱스에 간편하게 삽입하기 위한 0

for i in range(n):    
    index = nums[n-1-i]   //주어진 입력값을 뒤에서 부터 읽으면 해당 값이 인덱스 값이 됨
    l1 = l[:index]        //해당 위치에 삽입하기 위해 기존 배열 슬라이싱
    l2 = l[index:]
    l1.append(n-i)
    l = l1 + l2

for j in range(n):
    print(l[j], end=' ')

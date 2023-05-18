import sys
input = sys.stdin.readline

nums = input().rstrip()
countSixNine = 1
numCount = [0]*10             #사용한 방 번호의 수를 카운트해줄 배열

for num in nums:             
    numCount[int(num)] += 1 

countSixNine += numCount[6] + numCount[9]   #6과 9는 같이 사용할 수 있으므로 같이 더해줌
countSixNine //= 2                          #6과 9의 평균값

numCount[6] = countSixNine                  #6 카운트에 6과 9의 평균값
numCount[9] = countSixNine                  #9 카운트에 6과 9의 평균값

print(max(numCount))

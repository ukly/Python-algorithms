import sys
input = sys.stdin.readline

x = int(input())
sum = 0                                                       # / 대각선상에 있는 분수들의 개수의 합
i = 1                                                         # 대각선으로 몇번째 줄인지

while True:
    sum += i                                                  # i번째 줄에는 i개의 분수가 있으므로 i만큼 더함
    if sum > x:                                               # 타겟 x보다 합이 크면 타겟을 지나친 것
        sum -= i                                              # i만큼 다시 뒤로 가서 탐색 시작
        if i % 2 == 1:                                        # i가 홀수일때는 좌측 아래부터 대각선으로
            print(str(i - (x - sum) + 1) + "/" + str(x - sum))
        else:                                                 # i가 짝수일때는 우측 위부터 대각선으로
            print(str(x - sum) + "/" + str(i - (x - sum - 1)))
        break
    elif sum == x:                                            # 합이 타겟x와 일치한 경우
        if i % 2 == 0:
            print(str(i)+ "/1")
        else:
            print("1/" + str(i))
        break
    i += 1                                                    # 합이 타겟 x보다 작은 경우 i를 증가시켜 가며 진행

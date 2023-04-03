import sys
input = sys.stdin.readline

n = int(input())
result =0


for i in range(n):
    word = input().rstrip()
    try:
        if len(word) != 1:
            for j in range(len(word)-1):
                for k in range(j+2,len(word)):
                    if (word[j] == word[k]) and (word[j] != word[j+1]):     #불연속적으로 같은 문자가 나오는 경우에만 해당하므로
                        raise Exception                                     #j와 j랑 2이상 인덱스가 차이나는 k번째의 문자가 같으면서 j+1번째 문자가 일치하지 않는 경우를 탐색 
        result += 1
    except:
        pass

print(result)

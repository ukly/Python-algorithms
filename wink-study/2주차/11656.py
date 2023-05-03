import sys
input = sys.stdin.readline

word = input().rstrip()

words = [word[i:] for i in range(len(word))]    #문자를 시작 인덱스를 다르게하여 슬라이싱

sortedWords = sorted(words)         # 정렬

for sortedWord in sortedWords:
    print(sortedWord)

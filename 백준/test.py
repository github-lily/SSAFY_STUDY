import sys
sys.stdin = open('백준/test.txt')

N = int(input())

temp = [[] for _ in range(50)]      # 단어 길이 50 이하하
for _ in range(N) :
    word = input()
    temp[len(word)-1].append(word)  # 길이순 입력

# 사전순 정렬
for words in temp :
    test = ''                       # 중복 체크
    if words :                      # 값이 있을 때 확인
        for word in sorted(words) :
            if word != test :
                print(word)
                test = word
import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt')


def backtracking() :
    if N == 


T = map(int(input()))
for tc in range(1,T+1) :
    N = int(input())
    # 식재료 배열
    arr = [list(map(int,input.split())) for _ in range(N)]

    # 맛 점수 기록할 배열
    taste = [[0]*(N) for _ in range(N)]

    for r in range(N) :
        for c in range(N) :
            taste[r][c] = arr[r][c] + arr[c][r]
            taste[r][c] = taste[c][r]           # 대칭

    # 식재료 사용 표시 배열
    v = [0]*N

    for r in range(N) :
        for c in range(N) :

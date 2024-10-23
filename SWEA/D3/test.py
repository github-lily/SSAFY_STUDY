import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/SWEA/D3/test.txt')

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def dfs(x,y) :

    for i in range(4) :
        nr, nc = x+dr[i], y+dc[i]
        if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 1 :
            arr[nr][nc] = 0     # 재탐색하지 않도록 값 바꿔줌 
            dfs(nr,nc)


T = int(input())
for _ in range(T) :
    M, N, K = map(int,input().split())

    # 필요 변수 선언
    ans = 0
    arr = [[0] * M for _ in range(N)]

    # 배추 심기
    for _ in range(K) :
        X,Y = map(int,input().split())
        arr[Y][X] = 1

    # 배추밭 탐색
    for r in range(N) :
        for c in range(M) :
            if arr[r][c] == 1 :
                dfs(r,c)
                ans += 1

    print(ans)
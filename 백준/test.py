import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/portfolio/백준/test.txt")


def bfs(sr,sc,er,ec) :
    q = []
    v = [[0] * (M) for _ in range(N)]

    q.append((sr,sc))
    v[sr][sc] = 1


    dr = [1,0,-1,0]
    dc = [0,1,0,-1]

    while q :
        r,c = q.pop(0)
        if r == er and c == ec :
            return v[er][ec]
        
        for i in range(4) :
            nr,nc = r+dr[i], c+dc[i]
            if 0<=nr<N and 0<= nc < M and v[nr][nc] == 0 and arr[nr][nc] == 1 :
                v[nr][nc] = v[r][c]+1
                q.append((nr,nc))

            

N,M = map(int, input().split())
arr = [list(map(int,input())) for _ in range(N)]
ans = bfs(0,0,N-1,M-1)
print(ans)
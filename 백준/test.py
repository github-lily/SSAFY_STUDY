import sys
sys.stdin = open('백준/test.txt')


from collections import deque

dr, dc = [0,1,0,-1], [1,0,-1,0] # 우하좌상


def bfs(start) :
    q = deque()
    q.append(start)


    while q :
        r,c = q.popleft()

        for i in range(4) :
            nr, nc = r+dr[i], c+dc[i]
            if 0<= nr < N and 0<= nc < M :  # 범위 이내
                if map[nr][nc] == 0 :       # 벽이라면
                    route[nr][nc] = 0       # 벽 표시
                else :                      # 벽이 아닐 때
                    if route[nr][nc] == -1 : # 첫 방문이면
                        route[nr][nc] = route[r][c]+1       # 거리 표시
                        q.append((nr,nc))




N,M = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(N)]

route = [[-1]*M for _ in range(N)]


# 시작지점 찾기
for r in range(N) :
    for c in range(M) :
        if map[r][c] == 2 :
            start = (r,c)           # 시작지점 저장
            route[r][c] = 0         # 시작지점은 0
        if map[r][c] == 0 :
            route[r][c] = 0         # 반례 2 2 / 0 0 / 0 2 해결


bfs(start)

for line in route :
    print(*line)




import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt')


from collections import deque


def bfs(start) :
    global move

    union = [start]     # 연합 목록(나중에 연합 인구합 구할때 사용)
    q = deque()
    q.append(start)


    while q :
        ci,cj = q.popleft()
        for di,dj in (0,1),(1,0), (0,-1), (-1,0) :
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0 :
                if L <= abs(arr[ni][nj]-arr[ci][cj])<=R :
                    v[ni][nj] = 1
                    q.append((ni,nj))
                    union.append((ni,nj))
                    move += 1

    result = sum(arr[r][c] for r,c in union)//len(union)
    for r,c in union :
        arr[r][c] = result
    


N, L, R = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
days = 0


while True :
    days += 1
    v = [[0]* N for _ in range(N)]  #날 바뀔때마다 갱신
    move = 0            # 이동 여부 확인

    # 전체 배열을 순회하면서 연합국 찾기
    for r in range(N) :
        for c in range(N) :
            if v[r][c] == 0 :
                v[r][c] = 1
                bfs((r,c))

    if move == 0 :      # 인구이동이 없으면 종료
        days -= 1       # 하루 늘려줬던거 줄이고
        break

print(days)

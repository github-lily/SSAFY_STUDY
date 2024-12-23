import sys
sys.stdin = open('백준/test.txt')

# sys.stdin.readline 추가
# 223848KB, 684ms(PyPy3) 메모리 조오금 줄고 시간 조오금 늘어남. 유의미한 차이 없음
# unripen 추가하여 속도 향상 기대!


from collections import deque



def bfs() :
    
    q = deque()

    # 방향 저장(h,r,c) 위아래 상하좌우
    direction = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]


    unripe = 0

    # 익은 토마토 찾기
    for h in range(H) :
        for r in range(R) :
            for c in range(C) :
                if tomato[h][r][c] == 1 :
                    q.append((h,r,c,0))       # 0 : 시간
                elif tomato[h][r][c] == 0 :
                    unripe += 1
    
    if unripe == 0 :
        return 0


    # 토마토 숙성시키기
    while q :
        h, r, c, time = q.popleft()
        
        for dh,dr,dc in direction :
            nh,nr,nc = h+dh, r+dr, c+dc
            if 0<= nh < H and 0<= nr < R and 0<= nc < C and tomato[nh][nr][nc] == 0 :
                tomato[nh][nr][nc] = 1
                q.append((nh,nr,nc,time+1)) 


    # 탐색 끝나면 숙성안된 토마토가 남았는지 확인
    for h in range(H) :
        for r in range(R) :
            for c in range(C) :
                if tomato[h][r][c] == 0 :       # 고립된 토마토가 있다는 뜻
                    return -1
    
    return time



# 입력 처리
C, R, H = map(int, input().split())  # 열, 행, 층 개수 입력
# 3차원 배열로 토마토 상태 입력 받음
tomato = [ [list(map(int, input().split())) for _ in range(R)] for _ in range(H) ]

# BFS를 수행하여 결과 출력
print(bfs())


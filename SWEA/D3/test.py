import sys
sys.stdin = open("C:/Users/jhc03/Desktop/포트폴리오/SWEA/D3/test.txt")


'''
- RC카는 위를 보고있음
- 입력값
    - 필드의 크기 N, 벨 수 있는 횟수 K
    - 필드 정보(공백X), 풀 G, 나무 T, 현재위치 X, 목표 Y
- 출력값 :
    - 최소 리모컨 조작 횟수
    - 이동이 불가하다면 -1
'''

# X 위치 찾기
def start(sr,sc) : 
    for r in range(N) :
        for c in range(N) :
            if arr[r][c] == 'X' :
                sr,sc = r,c
                return sr,sc



# sr,sc : 시작점 , d : 현재 바라보는 방향, t : 나무 베기 남은횟수, cnt : 조작 횟수)
def kfc(sr,sc,d,t,cnt) :
    global min_cnt

    if arr[sr][sc] == 'Y' :
        if min_cnt > cnt :
            min_cnt = cnt
        return min_cnt
    
    if min_cnt < cnt :
        return

    for i in range(4) :
        nr,nc = sr+dr[i], sc+dc[i]
        if 0 <= nr < N and 0<= nc < N and v[nr][nc] == 0 :      # 범위 내, 방문한 적 없는 곳이라면
            if arr[nr][nc] == 'G' :      # 풀
                v[nr][nc] = 1
                d_cnt = abs(d-i)
                if d_cnt == 3 :     # |상-좌| = 3, 이 경우 반바퀴만 돌면 되니까 1
                    d_cnt = 1
                kfc(nr,nc,i,t,cnt+d_cnt+1)
                v[nr][nc] = 0


            if arr[sr][sc] == 'Y' :
                if min_cnt > cnt :
                    min_cnt = cnt
                return min_cnt
        

            else :                       # 나무
                if t> 0 :
                    v[nr][nc] = 1
                    d_cnt = abs(d-i)
                    if d_cnt == 3 :
                        d_cnt = 1
                    kfc(nr,nc,i,t-1,cnt+d_cnt+1)
                    v[nr][nc] = 0

    # 상우하좌가 모두 방문할 수 없으면 -1 리턴



T = int(input())
for tc in range(1,T+1) :
    N, K = map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    v = [[0]*N for _ in range(N)]   # 방문 배열
    min_cnt = 9999999999999999999999999999999999999999
    

    # 상우하좌(0,1,2,3)
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]


    sr,sc = start(0,0)
    v[sr][sc] = 1
    cnt = kfc(sr,sc,0,K,0)
    if min_cnt == 9999999999999999999999999999999999999999 :
        min_cnt = -1
    
    
    print(f'#{tc} {min_cnt}')


            





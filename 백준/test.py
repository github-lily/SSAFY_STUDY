import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt')

# 이동 방향 리스트 오른쪽, 대각선, 아래
di = [0,1,1]
dj = [1,1,0]



# 행, 열, 방향
def dfs(i,j,dir) :
    global cnt

    if i == N-1 and j == N-1 :
        cnt += 1
        return 


    for k in range(3) :
        ni,nj = i+di[k], j+dj[k]

        # 45도씩 움직일 수 있으므로 조건 걸어주기
        # 방향 제한 조건 (가로 -> 세로, 세로 -> 가로 불가)
        if (dir == 0 and k == 2) or (dir == 2 and k == 0) :
            continue

        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0 :       # 벽은 못감
            if k == 1 :     # 대각선일 경우 추가 벽 확인
                if arr[i][j+1] == 0 and arr[i+1][j] == 0 :  # 오른쪽 아래 벽인지 확인
                    dfs(ni,nj,k)
            else :
                dfs(ni,nj,k)

    
    

# 시작

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

cnt = 0

# 기준점을 끝으로 둠 (앞이 N,N에 닿을 가능성 0 (범위 벗어남))
# 행, 열, 놓인 방향(0 가로, 1 대각선, 2 세로)
# 시작점 0,1 (주의!)
dfs(0,1,0)

print(cnt)
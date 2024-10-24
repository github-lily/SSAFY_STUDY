import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt')


# dr = []

# T = int(input())
# for tc in range(1,T+1) :
#     N = int(input())
#     arr = [list(map(int,input().split())) for _ in range(N)]

#     ans = -1
#     for i in range(N) :
#         for j in range(N) :
#             dfs(i,j,[],0)
    
#     print(ans)



def dfs(r,c,cnt) :
    global ans, sr,sc, er, ec
    
    if cnt > ans :
        return
    
    if r == er and c == ec :
        ans = min(ans,cnt)
        return ans
    
    # 오른쪽과 아래만 확인하면 됨(우하)
    dr = [0,1]
    dc = [1,0]
    for i in range(2) :
        nr, nc = r + dr[i], c+dc[i]
        # 체스판의 범위 이내여야 함
        if sr<= nr <= er and sc<= nc <= ec :
            if arr[r][c] == arr[nr][nc] :   # 같다면
                cnt += 1
                if arr[r][c] == 'W' :
                    arr[nr][nc] = 'B'
                else :
                    arr[nr][nc] = 'W'
    
    


M,N = map(int,input().split())
arr = [list(input()) for _ in range(M)]
ans = 99999999999999999999999999999999999999999999999

for i in range(N) :
    for j in range(M) :
        # 오른쪽, 아래쪽으로 8x8을 만들 수 있을 때 dfs 호출
        # 종료를 위해 끝 지점 저장
        sr, sc = i,j
        er, ec = i+7, j+7
        if 0<= er <M and 0<=ec<N :
            dfs(i,j,0)

print(ans)

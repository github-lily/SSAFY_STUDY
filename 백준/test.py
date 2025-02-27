import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())


def dfs(n) :
    global ans


    if n == N :
        ans += 1
        return
    
    for j in range(N) :
        if v1[j] ==  v2[n+j] ==  v3[n-j] == 0 :
            v1[j] = v2[n+j] = v3[n-j] = 1
            dfs(n+1)
            v1[j] = v2[n+j] = v3[n-j] = 0

    

N = int(input())
ans = 0

# 가로 확인
v1 = [0] * N

# 우상 대각선 확인
v2 = [0] * (2*N) # 1 <= N <15 

# 좌상 대각선 확인
v3 = [0] *  (2*N)

dfs(0)

print(ans)
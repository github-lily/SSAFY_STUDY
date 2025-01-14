import sys
sys.stdin = open('백준/test.txt')


n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]


dp = [[0] * n for _ in range(n)]



dp[0][0] = arr[0][0]


for i in range(1,n) :
    dp[i][0] = dp[i-1][0] + arr[i][0]       # 맨 왼쪽
    dp[i][i] = dp[i-1][i-1] + arr[i][i]     # 맨 오른쪽
    for j in range(1,i) :
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]



print(max(dp[n-1]))


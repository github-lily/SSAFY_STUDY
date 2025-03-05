import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())
T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    if N == 1:
        print(max(arr[0][0], arr[1][0]))
        continue

    dp = [[0] * N for _ in range(2)]

    dp[0][0], dp[1][0] = arr[0][0], arr[1][0]
    dp[0][1], dp[1][1] = arr[0][1] + dp[1][0], arr[1][1] + dp[0][0]

    for j in range(2, N):
        dp[0][j] = arr[0][j] + max(dp[1][j-1], dp[1][j-2])
        dp[1][j] = arr[1][j] + max(dp[0][j-1], dp[0][j-2])

    print(max(dp[0][N-1], dp[1][N-1]))

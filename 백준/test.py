import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt')

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
INF = int(1e9)
ans = INF




# first : 첫번째 집의 색상
for first in range(3) :
    # 색상별로 최솟값을 기록해둘 배열
    dp = [[INF]*3 for _ in range(N)]
    dp[0][first] = arr[0][first]        # 첫번째로 칠할 집 색상만 기록
    
    # dp 테이블 채우기
    for i in range(1,N) :
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]



    # 첫번째 집의 색상과 마지막 집의 색상이 다를 때에만 결과 갱신
    for last in range(3) :
        if first != last :
            ans = min(ans,dp[N-1][last])

print(ans)
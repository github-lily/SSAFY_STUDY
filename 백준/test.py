import sys
sys.stdin = open('백준/test.txt')

N = int(input())
times = map(int,input().split())

times = sorted(times)

dp = [0]*N
dp[0] = times[0]
for i in range(1,N) :
    dp[i] = dp[i-1] + times[i]

print(sum(dp))
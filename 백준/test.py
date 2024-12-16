import sys
sys.stdin = open('백준/test.txt')


# 보텀업 방식(반복문 사용)

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [0] * 6

# dp 1과 2의 기본값 설정
dp[1] = dp[2] = 1
n = 5

# 피보나치 함수를 반복문으로 구현
for i in range(3, n+1) :
    dp[i] = dp[i-1] + dp[i-2]

print(dp[i])

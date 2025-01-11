import sys
sys.stdin = open('백준/test.txt')


s1 = input()
s2 = input()

n = len(s1)
m = len(s2)

dp = [0]*m

for i in range(n) :
    temp = 0
    for j in range(m) :
        if temp < dp[j] :
            temp = dp[j]        # 지금까지의 최대값 저장
        elif s1[i] == s2[j] :   # dp[j]의 값이 더 크다면 이미 계산된 글자이므로 elif(다시 계산할 필요 없음)
            dp[j] = temp + 1    

print(max(dp))
import sys
sys.stdin = open("백준/test.txt")

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coins = []
for _ in range(n) :
    coins.append(int(input()))

money = [0]*(k+1)
money[0] = 1

for coin in coins :
    for i in range(1,k+1) :
        if i-coin >= 0 :
            money[i] += money[i-coin]

print(money[-1])

# 백준 14502 연구소
'''
import sys, copy
input = sys.stdin.readline



N,M = map(int,input().strip().split())
arr = [list(map(int,input().strip().split())) for _ in range(N)]

# 0 빈 칸 / 1 벽 / 2 바이러스
# 1. 필요한 변수 : 벽의 개수 카운트
# 풀이 방법
# 1. 바이러스 찾기
# 2. 바이러스 근처 빈 벽 찾기
# 3. 빈 벽에 벽 세우기
# 4. 벽 개수가 0이 되면 안전 구역 cnt
# 5. 최고 안전구역 개수와 비교
# 3. 빈 벽이 한 개면 바로 막기 ( 벽 개수 -1 )
# 4. 빈 벽이 한 개 이상이면 
# 복잡하게 생각하지말고 걍 바로 bfs 돌려버려?

memo = copy.deepcopy(arr)

di,dj = [0,1,0,-1],[1,0,-1,0]
chance = 3


for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 2 :
            for k in range(4) :
                ni, nj = i + di[k] , j + dj[k]
                if arr[ni][nj] == 0 :
                    memo[ni][nj] = 1
                    chance -= 1
                    
'''
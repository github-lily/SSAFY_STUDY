import sys
sys.stdin = open("백준/test.txt")


import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

INF = int(1e9)
# 1번부터 시작
graph = [[INF] * (N+1) for _ in range(N+1)]

# 시작 == 도착 : 가중치 0
for k in range(1,N+1) :
    graph[k][k] = 0

# 간선 정보 입력
for _ in range(M) :
    s,e,v = map(int,input().split())
    # 노선이 여러개이므로 작은 값으로 저장
    if graph[s][e] >= v :
        graph[s][e] = v

for k in range(1,N+1) :
    for i in range(1,N+1) :
        for j in range(1,N+1) :
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,N+1) :
    for j in range(1,N+1) :
        if graph[i][j] == INF :
            print("0", end=" ")
        else :
            print(graph[i][j], end=" ")
    print()


# import sys
# input = sys.stdin.readline

# def check(r,c,size) :
#     color = arr[r][c]
#     for i in range(r,r+size) :
#         for j in range(c,c+size) :
#             if arr[i][j] != color :
#                 return False
#     return True

# def divide(r,c,size) :
#     global white, blue
#     if check(r,c,size) :
#         if arr[r][c] == 0 :
#             white += 1
#         else :
#             blue += 1
#         return
    
#     half = size // 2
#     divide(r, c, half)
#     divide(r, c+half, half)
#     divide(r+half, c, half)
#     divide(r+half, c+half, half)




# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]

# white = 0
# blue = 0

# divide(0,0,N)

# print(white)
# print(blue)

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
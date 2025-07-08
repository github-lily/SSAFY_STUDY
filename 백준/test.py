import sys
sys.stdin = open("백준/test.txt")


# import sys
# input = sys.stdin.readline

N,M = map(int,input().split())

if N > M :
    ans = (N-1) + ((M-1)*N)
else :
    ans = (M-1) + ((N-1)*M)

print(ans)

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
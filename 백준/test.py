import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt')


from collections import deque

# 네방향 탐색
di = [0,1,0,-1]
dj = [1,0,-1,0]


def bfs(i,j) :
    global village, house
    house = 1  # 새로운 단지를 탐색할 때 집의 수를 1로 초기화

    q = deque()
    q.append((i,j))
    v[i][j] = 1

    while q:
        ci,cj = q.popleft()
        for k in range(4) :
            ni,nj = ci+di[k], cj+dj[k]
            # 범위 내에 있고, 방문하지 않았고, 집이라면
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0 and arr[ni][nj] == 1 :
                v[ni][nj] = 1
                house += 1
                q.append((ni,nj))

    village += 1
    
    

N = int(input())
arr = [list(map(int,input())) for _ in range(N)]

v = [[0]*(N) for _ in range(N)]     # 방문 배열
village_house = []  # 단지별 집의 수 저장
village = 0         # 단지 수
house = 1           # 집의 수


for i in range(N) :
    for j in range(N) :
        if v[i][j] == 0 and arr[i][j] == 1 :
            bfs(i,j)
            village_house.append(house)
            house = 1       #집의 수 초기화(현재 위치도 집이므로 +1로 시작)
            # 키 값을 마을수로 정해서 자동 증가하도록 함



print(village)
village_house = sorted(village_house)
for home in village_house :
    print(home)

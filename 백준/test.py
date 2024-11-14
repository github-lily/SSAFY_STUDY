import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt')


import heapq

INF = int(1e9)

# 우하좌상 방향
di = [0,1,0,-1]
dj = [1,0,-1,0]

# 테스트케이스 넘버
tc = 0

while True :                # 테스트 케이스 개수가 주어지지 않음
    tc += 1                 # 테스트 케이스 +1
    N = int(input())
    if N == 0 : break       # 0이 입력되면 종료

    arr = [list(map(int,input().split())) for _ in range(N)]

    min_val = [[INF]*N for _ in range(N)]   # 최소 금액을 저장할 배열


    def dijkstra(si,sj) :
        q = []
        min_val[si][sj] = arr[si][sj]             # 주의할 점! : 이 문제는 0,0도 가중치가 있음
        heapq.heappush(q,(arr[si][sj],si,sj))     # 가중치, 시작점 좌표 # 가중치 값 주의


        while q :
            loss, ci,cj = heapq.heappop(q)
            
            # 목적지 도달
            if ci == N-1 and cj == N-1 : return


            # 손실 금액이 최소 손실 금액보다 크다면 pass
            if loss > min_val[ci][cj] : continue
            for k in range(4) :
                ni,nj = ci+di[k], cj+dj[k]
                if 0<= ni < N and 0 <= nj < N :     # 범위 이내일 때
                    go_loss = loss + arr[ni][nj]    # ni,nj에 가는데 드는 비용
                    if go_loss < min_val[ni][nj] :  # 새로운 값이 더 작다면
                        min_val[ni][nj] = go_loss   # 최소 비용 갱신
                        heapq.heappush(q,(go_loss,ni,nj))

    dijkstra(0,0)
    ans = min_val[N-1][N-1]
    print(f'Problem {tc}: {ans}')

            
            


            

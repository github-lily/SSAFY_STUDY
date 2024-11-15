import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/portfolio/백준/test.txt')



import heapq

V,E = map(int,input().split())
start = int(input())

INF = int(1e9)
# V개의 정점에서 V개의 정점으로 가는 최단경로 기록 리스트
min_val = [INF]*(V+1)

# 연결 관계를 담을 리스트(1번부터 시작)
lst = [[] for _ in range(V+1)]


for _ in range(E) :
    u,v,w = map(int,input().split())        # u에서 v로 가는 가중치 w
    lst[u].append((w,v))                    # 가중치, 연결 정점


def dijkstra(start) :
    q = []
    heapq.heappush(q,(0,start))         # 시작지점의 가중치 0과 시작지점
    min_val[start] = 0

    while q :
        cost, now  = heapq.heappop(q)

        # 이미 있는 최단경로보다 크다면 패스
        if cost > min_val[now] :
            continue

        # 현재 노드에서 다음 노드로 갈 때 필요한 임시 가중치 / 임시 지점
        for next_cost, next in lst[now] :
            go_cost = cost + next_cost       # pre 포인트로 갈 때 드는 총 가중치 = 현재 가중치 + (현재->다음 가중치)
            if go_cost < min_val[next] :
                min_val[next] = go_cost
                heapq.heappush(q,(go_cost,next))
            

# 다익스트라 호출
dijkstra(start)

# 출력
for k in min_val[1:] :      # 0번은 필요없는 값
    if k == INF :
        print('INF')
    else :
        print(k)

    

            
            


            

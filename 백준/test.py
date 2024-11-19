import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt')



import heapq


def dijkstra(start) :
    q = []
    heapq.heappush(q,(0,start))     # 가중치, 목적지
    dist[start] = 0

    while q :
        cost, now = heapq.heappop(q)

        if cost > dist[now] :
            return
        

        for go, go_cost in adj[now] :
            total_cost = dist[now] + go_cost
            if dist[go] > total_cost :
                dist[go] = total_cost
                heapq.heappush(q,(total_cost, go))



N = int(input())
M = int(input())

INF = int(1e9)
adj = [[] for _ in range(N+1)]  # 1번부터 시작, 연결 관계 저장 리스트
dist = [INF]*(N+1)              # 최소 비용 기록

for _ in range(M) :
    a,b,c = map(int,input().split())
    adj[a].append((b,c))
start,end = map(int,input().split())

dijkstra(start)

ans = dist[end]

print(ans)
import sys
sys.stdin = open('백준/test.txt')


from collections import deque


N,M,R = map(int,input().split())
adj = [[] for _ in range(N+1)]
visit = [0]*(N+1)

# 인접리스트 받기
for _ in range(M) :
    u,v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

# 오름차순으로 정렬
for edges in adj :
    edges.sort()


# 너비우선탐색
def bfs(start) :
    q = deque([start])
    order = 1
    visit[start] = order

    while q :
        c = q.popleft()
        
        for w in adj[c] :
            if visit[w] == 0 :
                order += 1
                visit[w] = order
                q.append(w)


bfs(R)

for i in range(1,N+1) :
    print(visit[i])



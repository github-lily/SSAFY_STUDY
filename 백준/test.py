import sys 
sys.stdin = open("백준/test.txt")

from collections import deque

N = int(input())


tree = [[] for _ in range(N+1)]
p = [0] * (N+1)


# 인접 노드 저장
for _ in range(N-1) :
    n1,n2 = map(int,input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)


# 트리 순회
def bfs(start) :
    q = deque([start])
    while q :
        current = q.popleft()
        for next in tree[current] :
            if p[next] == 0 :
                p[next] = current
                q.append(next)

bfs(1)

# 정답 출력
for i in range(2,N+1) :
    print(p[i]) 


# # 지수 찾는 함수
# def find(i,esp) :
    
#     while True :
#         if i < 2**esp :
#             return esp-1
#         esp += 1
    

# def check(n,m) :
#     # 지수 찾기
#     x = find(n,0)
#     y = find(m,0)

#     # 지수 그룹이 달라질때까지 계산
#     while True : 
#         # 지수 그룹이 다르면 큰 지수 그룹 
#         if x != y:
#             ans = max(x,y)
#             return ans
        
#         # 지수 그룹이 같으면 지수 그룹이 달라질때까지 계산 
#         else :
#             n = n - (2**(x-1))
#             m = m - (2**(x-1))
#             x = find(n,0)
#             y = find(m,0)

# length, n, m = map(int,input().split())

# ans = check(n,m)
# print(ans)

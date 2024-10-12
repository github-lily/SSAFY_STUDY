import sys
sys.stdin = open("C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt")


def dfs(n,s,lst) :

    if n == M :
        ans.append(lst)
        return
    
    if s > N :
        return

    for j in range(s,N+1) :
        dfs(n+1,j,lst+[j])

N,M = map(int,input().split())
ans = []

dfs(0,1,[])

for lst in ans :
    print(*lst)
import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/portfolio/백준/test.py")


def dfs(n,tlst) :
    if n == M :
        lst.append(tlst)
        return
    
    for i in range(N) :
        dfs(n+1,tlst+[nlst[i]])

N,M = map(int,input().split())
nlst = sorted(list(map(int,input().split())))
lst = []


for ans in lst :
    print(*ans)
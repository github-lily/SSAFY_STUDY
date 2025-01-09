import sys
sys.stdin = open('portfolio/백준/test.txt')



def dfs(n,tlst) :
    if len(tlst) == M :
        lst.append(tuple(tlst))
        return
    
    if n == N :
        return
    
    
    for i in range(N) :
        if v[i] == 0 :
            v[i] = 1
            dfs(n+1,tlst+[nlst[i]])
            v[i] = 0

        else :
            dfs(n+1,tlst)


N,M = map(int,input().split())
nlst = list(map(int,input().split()))
lst = []
v = [0]*N

dfs(0,[])

set_lst = set(lst)

ans_lst = sorted(list(set_lst))


for ans in ans_lst :
    print(*ans)



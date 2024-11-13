import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/portfolio/백준/test.txt')

def dfs(n,alst,blst) :
    global ans

    if n == N :                     #재료를 모두 다 담으면 
        return  
    
        if len(blst) == M :
            asum=bsum=0                 # 요리의 맛
            for i in range(M) :         # 재료 리스트의 개수가 M이므로 M까지
                for j in range(M) :
                    asum += arr[alst[i]][alst[j]]
                    bsum += arr[blst[i]][blst[j]]
            ans = min(ans,abs(asum-bsum))   
    
    # A 재료담기
    dfs(n+1,alst+[n],blst) 
    # B 재료담기
    dfs(n+1,alst,blst+[n]) 


T = int(input())
for tc in range(1,T+1) :
    N = int(input())
    M = N//2        # 요리 재료의 절반
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = 20000*N*N

    dfs(0,[],[])        #각 요리 재료를 담을 리스트
        

    print(f'#{tc} {ans}')
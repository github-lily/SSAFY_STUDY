import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt')




def bfs(k) :  
    score = 1       # 등수는 본인보다 큰 사람+1이므로 1로시작
    v = [0]*N

    v[k] = 1

    # 한명씩 비교해보기
    for w in range(N) :
        if v[w] == 0 :
            if info[k][0] < info[w][0] and info[k][1] < info[w][1] :
                score += 1
                v[w] = 1
    
    return score

N = int(input())
ranks = []      # 등수 리스트

# 몸무게와 키 정보를 담은 리스트
info = []
for _ in range(N) :
    w,h = map(int,input().split())
    info.append((w,h))

for k in range(N) :
    rank = bfs(k)
    ranks.append(rank)


print(*ranks)
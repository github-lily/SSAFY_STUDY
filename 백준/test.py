import sys
sys.stdin = open('백준/test.txt')


import heapq

N,K = map(int,input().split())

# 필요 변수 선언

INF = int(1e9)
time_lst = [[INF] * (max(N,K)*100)]
time = 0

def dijkstra(start) :
    q = heapq()
    heapq.heappush(q,(time,start))

    while q :
        sec, X = heapq.heappop(q)

        if sec > time_lst[X] :
            continue

        # 동생을 찾으면 종료
        if X == K :
            return

        elif 2*X == K :
            return
        
        elif X-1 == K or X+1 == K :
            if time_lst[K] > sec+1 :
                time_lst[K] = sec+1
            return
        
        # 동생을 못찾으면 탐색
        elif X-1 != K :
            if time_lst[X-1] > sec+1 :
                time_lst[X-1] = sec+1
            heapq.heappush(q,(sec+1,X-1))
        
        elif X+1 != K :
            if time_lst[X+1] > sec+1 :
                time_lst[X+1] = sec+1
            heapq.heappush(q,(sec+1,X+1))

        elif X*2 != K :
            if time_lst[X*2] > sec :
                time_lst[X*2] = sec
            heapq.heappush(q,(sec,X*2))
        

dijkstra(N)

ans = time_lst[K]

print(ans)


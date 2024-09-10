import sys
sys.stdin = open("C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt")


def superset(k,start,cur_sum) :
    global max_val

    if cur_sum > M :
        return

    if k == 3 :
        if max_val < cur_sum :
            max_val = cur_sum
        return cur_sum
    
    for i in range(N) :
        if visit[i] == 0 :
            visit[i] = 1
            path.append(cards[i])
            superset(k+1, i+1, cur_sum + cards[i])
            visit[i] = 0



N,M = map(int,input().split())
cards = list(map(int,input().split()))
visit = [0] * N
path = []

max_val = 0
superset(0,0,0)

print(max_val)
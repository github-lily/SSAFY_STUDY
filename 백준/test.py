import sys
sys.stdin = open('백준/test.txt')

import heapq

N = int(input())
q = []
for _ in range(N) :
    x = int(input())

    if x == 0 :
        if q :
            print(heapq.heappop(q)[1])

        else :
            print(0)
    else :
        heapq.heappush(q,(abs(x),x))
    



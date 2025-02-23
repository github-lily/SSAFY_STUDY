import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())

import sys
import heapq

input = sys.stdin.readline
q = []

N = int(input().strip())

for _ in range(N) :
    x = int(input().strip())

    if x == 0 :
        if q :
            print(-heapq.heappop(q))
        else :
            print(0)

    else :
        heapq.heappush(q, -x)
        


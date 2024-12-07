import sys
sys.stdin = open('백준/test.txt')


import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
q = deque()
ans = 0

for _ in range(N) :
    command = input().split()

    if len(command) > 1 :
        x = int(command[1])
        q.append(x)
        
    else :
        if command[0] == 'pop' :
            if q :
                ans = q.popleft()
            else :
                ans = -1

        elif command[0] == 'size' :
            ans = len(q)

        elif command[0] == 'empty' :
            if q :
                ans = 0
            else :
                ans = 1
        
        elif command[0] == 'front' :
            if q :
                ans = q[0]
            else :
                ans = -1

        
        elif command[0] == 'back' :
            if q :
                ans = q[-1]
            else :
                ans = -1

        print(ans)



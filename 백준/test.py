import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())

from collections import deque

N = int(input())
q = deque()

for _ in range(N) :
    cmd = list(map(int,input().split()))

    if cmd[0] == 1 :
        q.appendleft(cmd[1])
    
    elif cmd[0] == 2 :
        q.append(cmd[1])
    
    elif cmd[0] == 3 :
        if q :
            num = q.popleft()
            print(num)
        else :
            print(-1)
    
    elif cmd[0] == 4 :
        if q :
            num = q.pop()
            print(num)
        else :
            print(-1)
    
    elif cmd[0] == 5 :
        len = len(q)
        print(len)

    elif cmd[0] == 6 :
        if q :
            print(0)
        else :
            print(1)
    
    elif cmd[0] == 7 :
        if q :
            q.
        



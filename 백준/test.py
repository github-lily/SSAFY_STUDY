import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())
import sys

# 입력 받기
N = int(input())
stack = []

for _ in range(N) :
    cmd = list(map(int,sys.stdin.readline().split()))


    if cmd[0] == 1 : # push
        stack.append(cmd[1])

    elif cmd[0] == 2 : # pop
        if stack :
            print(stack.pop())
        else :
            print(-1)
    
    elif cmd[0] == 3 : # size
        print(len(stack))

    elif cmd[0] == 4 : # empty
        if stack :
            print(0)
        else :
            print(1)

    elif cmd[0] == 5 : # top
        if stack :
            print(stack[-1])
        else :
            print(-1)


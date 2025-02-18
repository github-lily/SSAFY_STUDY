import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())
import sys


def check(value) :
    for i in value :
        if i == '(' :
            stack.append(i)
        else :
            if stack :
                stack.pop()
            else :
                print("NO")
                return
    if stack :
        print("NO")
        return
    else :
        print("YES")
        return

# 입력 받기
N = int(input())
for _ in range(N) :
    stack = []
    val = list(input())

    check(val)

    



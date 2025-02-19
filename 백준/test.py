import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())
import sys


def check(value) :
    stack = []
    for i in value :
        if i == '(' or i == '[' :
            stack.append(i)
        elif i == ')' :
            if stack :
                j = stack.pop()
                if j != '(' :
                    print("no")
                    return
            else :
                print("no")
                return
                
        elif i == ']' :
            if stack :
                j = stack.pop()
                if j != '[' :
                    print("no")
                    return
            else :
                print("no")
                return
    if stack :
        print("no")
        return
    else :
        print("yes")
        return

# 입력 받기

import sys
while True :
    text = sys.stdin.readline().rstrip()
    if text == "." :
        break

    check(text)

    



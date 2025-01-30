import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())


while True :
    a,b = map(int,input().split())
    if a == b == 0 :
        break

    if a > b :
        print('Yes')
    else :
        print('No')
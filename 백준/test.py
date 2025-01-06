import sys
sys.stdin = open('백준/test.txt')


N = int(input())

cnt = 0

while N > 1 :
    
    if N % 3 == 0 :
        N = N // 3
        cnt += 1
    
    elif N % 2 == 0 :
        N = N // 2
        cnt += 1

    
    else :
        N = N - 1
        cnt += 1


print(cnt)


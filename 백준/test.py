import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt')

T = int(input())
max_val = 0
for _ in range(T) :
    a,b,c = map(int,input().split())

    if a == b == c :
        ans = 10000+(a*1000)
    elif a == b or a == c :
        ans = 1000+(a*100)
    elif b == c :
        ans = 1000+(b*100)
    else :
        ans = max(a,b,c)*100

    if max_val < ans :
        max_val = ans

print(max_val)
    
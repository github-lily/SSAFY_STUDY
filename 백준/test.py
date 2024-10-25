import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt')


N = int(input())
arr = list(map(int,input().split()))
v = int(input())


ans = 0
for num in arr :
    if num == v :
        ans += 1

print(ans)



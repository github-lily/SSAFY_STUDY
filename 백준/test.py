import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())

k,n,m = map(int,input().split())


ans = k*n-m
if ans >=0 :
    print(ans)
else :
    print(0)
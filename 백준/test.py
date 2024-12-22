import sys
sys.stdin = open('백준/test.txt')


N,M = map(int,input().split())
lst = list(map(int,input().split()))
for _ in range(M) :
    s,e = map(int,input().split())
    print(sum(lst[s-1:e]))
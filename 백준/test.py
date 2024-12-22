import sys
sys.stdin = open('백준/test.txt')


import sys
input = sys.stdin.readline

N,M = map(int,input().split())
lst = [0] + list(map(int,input().split()))


sum_lst = [0]*(N+1)
sum_lst[1] = lst[1]

for i in range(2,N+1) :
    sum_lst[i] = sum_lst[i-1]+lst[i]


for _ in range(M) :
    s,e = map(int,input().split())
    print(sum_lst[e]-sum_lst[s-1])

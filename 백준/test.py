import sys
sys.stdin = open('백준/test.txt')


N = int(input())
for i in range(1,N+1) :
    print('*'*i)
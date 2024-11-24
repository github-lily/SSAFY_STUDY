import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt')


T = int(input())
for _ in range(T) :
    a,b = map(int,input().split())
    print(a+b)
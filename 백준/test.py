import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt')


T = int(input())
for tc in range(1,T+1) :
    A,B = map(int,input().split())
    ans = A+B


    print(f'Case #{tc}: {A} + {B} = {ans}')
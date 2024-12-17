import sys
sys.stdin = open('백준/test.txt')

input = sys.stdin.readline

while input :
    A,B = map(int,input().split())
    print(A+B)
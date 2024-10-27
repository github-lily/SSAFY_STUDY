import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt')


N = int(input())
arr = list(map(int,input().split()))

min_v = min(arr)
max_v = max(arr)
print(f'{min_v} {max_v}')
import sys
sys.stdin = open('백준/test.txt')

n = int(input())
lst = list(map(int,input().split()))

print(max(lst)* min(lst))

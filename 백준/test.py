import sys
sys.stdin = open('백준/test.txt')


import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
print(pow(a, b, c))
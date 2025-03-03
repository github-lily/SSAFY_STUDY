import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())
a,b = map(int,input().split())
print(a+b)
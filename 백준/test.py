import sys
sys.stdin = open('백준/test.txt')

N = int(sys.stdin.readline().strip())

for _ in range(N) :
  a,b = map(int,sys.stdin.readline().strip().split())
  print(a+b)
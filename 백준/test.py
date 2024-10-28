import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt')




t = int(input())

for _ in range(t):
  n = int(input())
  ctx = {}

  for _ in range(n):
    s, l = input().split()

    ctx[s] = ctx.get(s, 0) + int(l)

  print(max(ctx, key=ctx.get))
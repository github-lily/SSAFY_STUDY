import sys
sys.stdin = open('백준/test.txt')


N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
arr2 = [list(map(int,input().split())) for _ in range(N)]


for i in range(N) :
  for j in range(M) :
    arr[i][j] += arr2[i][j]

for line in arr :
  print(*line)
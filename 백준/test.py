import sys
sys.stdin = open('백준/test.txt')

N = int(sys.stdin.readline().strip())


for _ in range(N) :
  x,y = map(int,sys.stdin.readline().strip().split())

  x = x%10
  if x == 0 :
    print(10)
    continue


  cycle = []
  temp = x
  while temp not in cycle :
    cycle.append(temp)
    temp = (temp * x) % 10

  
  idx = (y-1) % len(cycle)
  print(cycle[idx])
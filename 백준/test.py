import sys
sys.stdin = open('백준/test.txt')

arr = [list(map(int,input().split())) for _ in range(9)]
max_val = -1
max_point = [0,0]

for i in range(9) :
  for j in range(9) :
    if max_val < arr[i][j] :
      max_val = arr[i][j]
      max_point = [i+1,j+1]

print(max_val)
print(*max_point)
import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())
N = int(input())
adj = [list(map(int,input().split())) for _ in range(N) ]

arr = [row[:] for row in adj]

for k in range(N) :
    for i in range(N) :
        for j in range(N) :
            if (arr[i][j] == 1) or (arr[i][k] == 1 and arr[k][j] == 1) :
                arr[i][j] = 1


for line in arr :
    print(*line)
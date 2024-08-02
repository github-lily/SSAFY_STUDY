import sys
sys.stdin = open('sort.txt')

T = int(input())

for t in range(1, T+1):
    n = int(input())

    arr = list(map(int, input().split()))

    for i in range(n, 0, -1):
        for j in range(0, i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(f'#{t}', *arr)
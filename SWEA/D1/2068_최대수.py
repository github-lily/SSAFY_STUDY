T = int(input())
for tc in range(1,T+1) :
    arr = list(map(int,input().split()))

    max_val = 0
    for i in range(10) :
        if arr[i] > max_val :
            max_val = arr[i]

    print(f'#{tc} {max_val}')

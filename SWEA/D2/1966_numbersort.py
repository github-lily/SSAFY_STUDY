#11151. 이웃 원소의 합

T = int(input())



for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    sum_list = []
    for s in range(0,N-1) :
        sum = arr[s]+arr[s+1]
        sum_list.append(sum)

    #최대값 구하기
    max_v = sum_list[0]
    for i in range(len(sum_list)) :
        if sum_list[i] > max_v :
            max_v = sum_list[i]

    print(f'#{tc} {max_v}')


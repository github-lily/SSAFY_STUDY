T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    li = list(map(int, input().split()))

    # sum_li = [0] * N
    # sum_li[0] = li[0]
    # for i in range(1, N): #구간합으로 저장한 리스트
    #     sum_li[i] = sum_li[i-1] + li[i]
    temp = []

    for i in range(0, N-M+1):
        temp_sum = 0
        for j in range(M):
            temp_sum += li[i+j]
        temp.append(temp_sum)

    t_max = temp[0]
    t_min = temp[0]
    for t in temp:
        if t >= t_max:
            t_max = t
        if t <= t_min:
            t_min = t

    print(f'#{tc} {t_max - t_min}')
T = int(input())        #테스트케이스의 개수



for tc in range(1,T+1) :
    N = int(input())  # 2차원 배열의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]  # N개의 정수  N개 줄만큼

#인접행렬의 i,j값
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    max_v = 0
    for i in range(N) :
        for j in range(N) :
            near_sum = arr[i][j]
            for k in range(4):
                ni = i+di[k]
                nj = j+dj[k]
                if 0<=ni<N and 0<=nj<N :
                    near_sum = near_sum + arr[ni][nj]
            if max_v <near_sum :
                max_v = near_sum

    print(f'#{tc} {max_v}')




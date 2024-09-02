'''
1. NxN 칸으로 구분된 실험판
2. 어떤 칸에 올려두면 그 칸을 포함해 인접 칸의 먹이를 모두 먹음
3. 인접칸 : 상하좌우
4. 가장자리는 칸이 적음(if 조건걸기)
5. 먹이를 가장 많이 먹을 수 있는 최대 양 구하기
6. 합계가 음수인 경우 절대값이 작은 쪽이 답(그냥 연산이랑 똑같음)

'''




T = int(input())
for tc in range(1,T+1) :
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_food = -9999
    for i in range(N) :
        for j in range(N) :

            food_sum = 0
            ni = [0,1,0,-1]     #우하좌상의 i 인덱스
            nj = [1,0,-1,0]     #우하좌상의 j 인덱스
            for x in range(4) :
                if 0 <= i+ni[x] < N and 0 <= j+nj[x] < N :        #가장자리 칸 범위 벗어나지 않도록 조건
                    food_sum += arr[i+ni[x]][j+nj[x]]
            food_sum += arr[i][j]           # 가운데값 더해주기
            #최대값 구하기
            if max_food < food_sum :
                max_food = food_sum


    #값 출력
    print(f'#{tc} {max_food}')

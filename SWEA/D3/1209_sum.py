T = int(input())

for tc in range(1,T+1) :
    # arr = [list(map(int,input().split())) for _ in range(100)]      #100x100 행렬
    
    arr = [[4, 4, 3, 2, 1, 2, 2, 1, 6, 5, 3, 5, 4, 6, 7, 4, 2, 5, 9, 7, 8, 1, 9, 5, 6] for _ in(5)]

    max_sum = 0     #최대값
    #각 행의 합(row) #각 열의 합(column)    

    for i in range(5) :
        row_sum = 0
        col_sum = 0
        for j in range(5) :
            row_sum += arr[i][j]        #행 우선순회
            col_sum += arr[j][i]        #열 우선순회
        if max_sum < row_sum :      #행의 합 중 최댓값 찾기
            max_sum = row_sum       #한 행의 합이 구해진 후 비교! 들여쓰기 주의
        elif max_sum < col_sum :    #열의 합 중 최대값 찾기
            max_sum = col_sum


    #대각선의 합 (diagonal)
    #좌에서 우측방향 대각선
    dia_sum_LR = 0
    for i in range(5) :
        dia_sum_LR += arr[i][i]
        if max_sum < dia_sum_LR:
            max_sum = dia_sum_LR



    # 우에서 좌방향 대각선
    dia_sum_RL = 0
    for i in range(5) :
        dia_sum_RL += arr[i][99-i]      #그림그리면 이해됨^^ㅠ index로 볼 때 i+j = 99 즉 j = 99-i
        if max_sum < dia_sum_RL :
            max_sum = dia_sum_RL



    #결론
    print(f'#{tc} {max_sum}')




    # #각 열의 합(column) - 열우선순회 #런타임오류로 위 코드랑 합침
    # col_sum = 0
    # for j in range(100) :
    #     for i in range(100) :
    #         col_sum += arr[i][j]
    #         if max_sum < col_sum :
    #             max_sum = col_sum


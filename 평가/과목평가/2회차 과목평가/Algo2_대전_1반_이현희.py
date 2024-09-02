'''
1. 김싸피는 완만한 오르막길을 좋아함
2. 전체 경로 길이가 N
3. 김싸피가 가장 좋아하는 오르막길의 길이를 출력(가장 낮은 경사도의 길이 출력)

- 등산 경로의 지형은 정수 배열 형태로 주어짐
- 오르막길은 이전 위치보다 높거나 같은 경우 계속 이어지는 것
- 경사도 : 오르막길에서 가장 높은 높이 A와 가장 낮은 높이 B의 차에서 경로 길이 C를 나눈 값
- 경사도가 같은 경우 오르막 길이가 긴 경로의 길이를 출력(부동소수점 오류 생각안해도 됨)
- 오르막의 최소 길이는 2
- 만약 오르막이 없는 경우 0을 출력

1. 만약 [i+1] 이 [i] 보다 작으면 내리막길, 계속 그러면 0 출력
2. [i+1]이 [i]보다 큰 경우 cnt += 1
3. 경사도(hill) : (max[i] - min[i])/c
4. low_hill 변수로 경사로 최소값 찾기
5. 경사도가 같은 경우 if 문 사용해서 max_cnt로 비교해서 최대값 찾기
6. 인덱스로 접근하기

'''


T = int(input())
for tc in range(1,T+1) :
    N = int(input())
    arr = list(map(int,input().split()))



    max_cnt = 0
    for i in range(N-1) :
        while True :
            cnt = 1
            max_i = 0
            min_i = N // 2
            if arr[i] <= arr[i+1] :
                cnt += 1    #길이 구하기
                #최대 높이 구하기
                if arr[max_i] < arr[i+1] :
                    max_i = i+1
                #최소 높이 구하기
                if arr[min_i] > arr[i] :
                    min_i = i
            if max_cnt < cnt:
                    max_cnt = cnt
            else :
                break
        low_hill = 999
        hill = (arr[max_i] - arr[min_i])/cnt
        if low_hill > hill :
            low_hill = hill
            best = cnt

    print(f'#{tc} {best}')


    #
    #
    # cnt = 1                         #오르막길 길이
    #
    # max_i = 0                      #높이 최대 인덱스
    # min_i = N//2                      #높이 최소 인덱스
    # i = 0
    # while arr[i] <= arr[i+1] and i < N :
    #     if
    #
    #
    # for i in range(N-1) :           #기준값의 범위 0부터 N-2까지
    #     while arr[i] <= arr[i+1] :
    #         cnt += 1
    #         if arr[max_i] < arr[i + 1]:  # 오르막길 최대값 구하기
    #             max_i = i + 1
    #         if arr[min_i] > arr[i]:  # 내리막길 최소값 구하기
    #             min_i = i
    #         # 최소 경사도 구하기
    #         low_hill = 999  # 경사로 최소값, 오르막길이 없는 경우 0 출력
    #         hill = (arr[max_i] - arr[min_i]) / cnt
    #         best = 0  # 최저 경사로의 길이(찾는 값)
    #         if low_hill > hill:
    #             low_hill = hill
    #             best = cnt
    #     else :
    #         pass
    #
    #     print(f'#{tc} {best}')
    #
    #
    #





    # cnt = 1                         #오르막길 길이
    #
    # max_i = 0                      #높이 최대 인덱스
    # min_i = N//2                      #높이 최소 인덱스
    # for i in range(N-1) :           #기준값의 범위 0부터 N-2까지
    #     if arr[i] <= arr[i+1] :     #오르막길일 때
    #         cnt += 1                #길이 +1
    #         if arr[max_i] < arr[i+1] :      #오르막길 최대값 구하기
    #             max_i = i+1
    #         if arr[min_i] > arr[i] :        #내리막길 최소값 구하기
    #             min_i = i
    #     #최소 경사도 구하기
    #         low_hill = 999  # 경사로 최소값, 오르막길이 없는 경우 0 출력
    #         hill = (arr[max_i] - arr[min_i]) / cnt
    #         best = 0        #최저 경사로의 길이(찾는 값)
    #         if low_hill > hill :
    #             low_hill = hill
    #             best = cnt
    #
    #
    # print(f'#{tc} {best}')







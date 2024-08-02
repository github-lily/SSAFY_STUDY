T = int(input())


for tc in range(1, T+1) :
    N, M = map(int, input().split())
    arr = list(map(int,input().split()))



    #구간별 최대값 구하기
    sum = 0
    sum_list = []
    for s in range(0, N-M+1) :          # s : 구간의 시작점. M개의 요소를 더할 때 사용할 인덱스
        for i in range(s, s+M) :        #시작점부터  m개의 요소를 더하는 부분
            sum += arr[i]
        sum_list.append(sum)
        sum = 0


        #합계 리스트에서 최대값 찾기
        max_v = 0

        for sum_v in sum_list :
            if sum_v > max_v :
                max_v = sum_v

        #합계 리스트에서 최소값 찾기
        min_v = sum_list[0]
        for sum_v in sum_list:
            if sum_v < min_v:
                min_v = sum_v

    result = max_v-min_v
    print(f'#{tc} {result}')





#
# 1. s부터 s+M-1 까지 더함
# 2. 더한 값을 빈 리스트에 할당
# 3. 제일 큰 값 뽑기
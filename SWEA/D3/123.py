T = int(input()) # 테스트 케이스 수 입력
for tc in range(1, T + 1): # 각 테스트 케이스에 대한 반복문
    N = int(input()) # 배열의 크기 입력
    arr = list(map(int, input().split())) # 배열 입력 받기

    for i in range(10): # 10개 요소 정렬
        min_idx = i # min_idx와 max_idx를 현재 인덱스 i로 초기화한다.
        max_idx = i
        for j in range(i + 1, N): 
            if arr[max_idx] < arr[j]: # 최대값 인덱스 찾기
                max_idx = j
            if arr[min_idx] > arr[j]: # 최소값 인덱스 찾기
                min_idx = j

        if i % 2 == 0: # 짝수일 떄 최대값과 교체
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        else: # 홀수일 때 최소값과 교체
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    result = arr[:10]  # 첫 10개의 요소 저장
    print(f'#{tc}', *result) # 결과 출력

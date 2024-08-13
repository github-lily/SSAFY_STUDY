# 배열2_특별한정렬_확인용

import sys
sys.stdin = open("12392.txt", "r")

'''
N개의 정수가 주어지면 가장 큰 수, 가장 작은 수 , 2번째 큰 수, 2번째 작은 수 식으로 번갈아 정렬
N = 정수의 개수
'''

'''
1. i 값(맨첨엔 맨 좌측 값)을 최대값으로 잡고, 우측에서 최대값을 찾은 뒤 최대값이 좌측으로 가게 한다
2. 그 다음 2번째 값(i+1)에서 최소값을 찾고, i+1 과 값을 바꾼다
인덱스가 짝수일 때 최대값 홀수일 때 최소값을 번갈아가면서 쓰면 된다!!!
'''


T = int(input())

for tc in range(1,T+1) :
    N = int(input())
    arr = list(map(int,input().split()))
    for i in range(N-1) :
        if i % 2 == 0 :     #i가 짝수일 때 최대값 찾기
            max_idx = i
            for j in range(i+1,N) :
                if arr[max_idx] < arr[j] :
                    max_idx = j
            arr[i],arr[max_idx] = arr[max_idx], arr[i]

        else :
            min_idx = i
            for j in range(i+1,N) :
                if arr[min_idx] > arr[j] :
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    result = arr[:10]
    print(f'#{tc}', *result)
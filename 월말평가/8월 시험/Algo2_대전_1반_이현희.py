
'''
- N명의 외계인 줄세우기
- A = 0, B = 1, C = 2
- 위험도 : arr[앞,뒤]
- 위험도 값은 모두 다르다
- 줄을 잘 세웠을 때의 최소 위험도는?

위험도 :
i,j + j,k

순열 최소합 구하기 문제

<풀이 방법>
1. 인덱스 번호를 담은 중복 없는 순열 만들기
2. 순열을 하나씩 가져와서 위험도 구하기
3. 그 위험도를 최소 위험도와 비교하며 값 갱신하기
4. 최소 위험도 출력

N의 수에 따라 구해야함...

'''


# 1차 배열에서의 순열 구하는 함수
def find_powerset(lst) :
    power_set = []      #[[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
    for i in range(N) :
        for j in range(N) :
            if man[j] != man[i] :
                for k in range(N) :
                    if man[k] != man[i] and man[k] != man[j] :
                        power_set.append([i,j,k])

    return power_set


T = int(input())
for tc in range(1,T+1) :
    N = int(input())        # 외계인의 수
    arr = [list(map(int,input().split())) for _ in range(N)]

    min_danger = 999999999999     # 최소값


    # 순열 만들기
    man = list(range(N))    #외계인 번호(인원수만큼 만들어야함)
    case = find_powerset(man)   #순열


    # 2차 배열에서의 순열 최소합 구하기
    for idx in case :       # 순열에서 하나씩 빼옴
        danger = 0
        for v in range(N-1) :
            danger += arr[idx[v]][idx[v+1]]  # 위험도
        # 최소 위험도 구하기
        if min_danger > danger :
            min_danger = danger


    # 답 출력
    print(f'#{tc} {min_danger}')
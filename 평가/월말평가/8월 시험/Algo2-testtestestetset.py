import sys
sys.stdin = open("algo2_sample_in.txt")

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

'''

def find_set(lst,k,n) :
    powerset = []
    visit = []
    if k == n :
        return powerset
    else :
        for i in range(n) :
            if i in visit :     # 사용했었던 값이라면
                continue        # 넘어감
            else :              # 사용 안 한 값이라면
                powerset.append(i)
                find_set(lst,k+1,n)
                visit = []




# # 1차 배열에서의 순열 구하는 함수
# def find_powerset(lst) :
#     power_set = []      #[[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
#     for i in range(N) :
#         for j in range(N) :
#             if man[j] != man[i] :
#                 for k in range(N) :
#                     if man[k] != man[i] and man[k] != man[j] :
#                         power_set.append([i,j,k])
#
#     return power_set



def find_set(lst,k,n) :
    visit = []
    power_set = []

    if k == n :
        return print(power_set)
    else :
        for i in range(n) :
            if i in visit :
                    continue
            else :
                power_set.append(i)
                find_set(lst,k+1,n)




T = int(input())
for tc in range(1,T+1) :
    N = int(input())        # 외계인의 수
    arr = [list(map(int,input().split())) for _ in range(N)]

    min_danger = 999999999999     # 최소값


    # 순열 만들기
    man = list(range(N))    #외계인 번호(인원수만큼 만들어야함)
    case = find_set(man,0,N)   #순열

    print(case)
    #
    # # 2차 배열에서의 순열 최소합 구하기
    # for idx in case :       # 순열에서 하나씩 빼옴
    #     danger = arr[idx[0]][idx[1]] + arr[idx[1]][idx[2]]  # 위험도
    #     # 최소 위험도 구하기
    #     if min_danger > danger :
    #         min_danger = danger


    # 답 출력
    # print(f'#{tc} {min_danger}')
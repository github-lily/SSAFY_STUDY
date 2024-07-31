T = int(input())        #테스트 케이스의 수
A = [1,2,3,4,5,6,7,8,9,10,11,12]     # 집합 A

for tc in range(1,T+1) :
    N, K = map(int,input().split())     #N : 원소의 개수 , K 원소의 합
    all_set = [] #a의 부분집합

    #집합 A의 부분집합 구하기
    for i in range(1<<N) :
        for j in range(N) :
            if i & (1<<j) :
                all_set.append()
        print()
    print(all_set)

    cnt = 0
    for k in all_set:
;
        total = 0
        for m in str(k) :
            total += int(k)

        if len(k) == N and total == K :
            cnt += 1

    print(cnt)

    # print(f'#{tc} {cnt}')
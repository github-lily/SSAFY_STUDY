#평균값 구하기

T = int(input())
for t in range(1,T+1):
    val = list(map(int, input().split()))
    val_sum = 0
    for i in range(len(val)):
        val_sum = val_sum + val[i]
    aver = int(round(val_sum/len(val),0))
    #round(반올림하려는 수, 자리수-1) : 반올림해주는 함수
    print(f'#{t} {aver}')



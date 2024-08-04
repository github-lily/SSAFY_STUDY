T = int(input())

for tc in range(1,T+1) :
    case = list(input())
    N = len(case)
    for i in range(N//2) :
        if case[i] == case[N-1-i] :
             result = 1
        else :
            result = 0
    print(f'#{tc} {result}')
            
        


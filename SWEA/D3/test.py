import sys
sys.stdin = open("C:/Users/jhc03/Desktop/포트폴리오/SWEA/D3/test.txt")


'''
- 배열 순회하면서 연속이 아닌 값이 나오면 중단

'''

# 행 확인
def check_row(s,e) :
    global ans
    for k in range(1,4) :
        if e+k >= 4 or e+k < 0 :
            return False
        if arr[s][e] != arr[s][e+k] :
            if arr[s][e+k] != 'T' :
                return False
    ans = arr[s][e]
    return ans 

# 열 확인
def check_col(s,e) :
    global ans
    for k in range(1,4) :
        if 0 <= s+k < 4 :
            if arr[s][e] != arr[s+k][e] :
                if arr[s][e+k] != 'T' :
                    return False
    ans = arr[s][e]
    return ans 

# 왼쪽에서 오른쪽 대각선
def l_to_r(s,e) :
    global ans
    for k in range(1,4) :
        if 0<= s+k < 4 and 0 <= e+k < 4 :
            if arr[s][e] != arr[s+k][e+k] :
                if arr[s][e+k] != 'T' :
                    return False
    ans = arr[s][e]
    return ans 


# 오른쪽에서 왼쪽 대각선
def r_to_l(s,e) :
    global ans
    for k in range(1,4) :
        if 0<= s+k < 4 and 0 <= e-k < 4 :
            if arr[s][e] != arr[s+k][e-k] :
                if arr[s][e+k] != 'T' :
                    return False
    ans = arr[s][e]
    return ans 



T = int(input())
for tc in range(1,T+1) :
    arr = [list(input()) for _ in range(4)]
    ans = ''
    dot = 0

    for r in range(4) :
        for c in range(4) :
            if arr[r][c] == '.' :
                dot = 1
            else :
                check_row(r,c)
                if ans == False :   
                    check_col(r,c)
                    if ans == False :
                        l_to_r(r,c)
                        if ans == False :
                           r_to_l(r,c)
                        else :      # 답을 찾으면 탐색 중단
                            break
        if not ans :    #답을 찾으면 탐색 중단
            break
    
    if ans :            # 반복이 끝나도 답을 못찾았다면
        if dot == 0 :    # 점이 없다면
            print(f'#{tc} Draw')
        else :
            print(f'#{tc} Game has not completed')
    else :              # 답을 찾았다면
        print(f'#{tc} {ans} won')

import sys
sys.stdin = open("C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt")

# SWEAR 13732 정사각형 판정 문제와 비슷함


# 너비 구하기
def check_row(sr,sc) :
    global row
    for r in range(sr+1,10) :
        if arr[r][sc] == 1 :
            row += 1
        else :
            break
    return row

def check_col(sr,sc) : 
    global col
    for c in range(sc+1,10) :
        if arr[sr][c] == 1 :
            col += 1
        else :
            break
    return col
    

# 네모 확인
def check_rec(sr,sc) :
    for r in range(sr+1,10) :
        for c in range(sc+1,10) :
            if arr[r][c] == 0 :
                

arr = [list(map(int,input.split())) for _ in range(10)]



sr,sc = 10,10       # 좌상단
er,ec = -1,-1       # 우하단
for i in range(10) :
    for j in range(10) :
        row = 1
        col = 1
        if arr[i][j] == 1 :
            check_row(i,j)
            check_col(i,j)
            if row == col :
                check_rec(i,j)
            



        

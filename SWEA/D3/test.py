import sys
sys.stdin = open("C:/Users/jhc03/Desktop/포트폴리오/SWEA/D3/test.txt")


'''
- #을 만나면 좌우 길이를 확인(1이면 안됨)
- 좌우가 맞으면 네모가 모두 잘 채워져있는지 확인
'''


def check_len(sr,sc) :
    global cnt
    for k in range(1,N) :
        nr, nc = r+k,c+k
        if 0 <= nr < N and 0 <= nc < N :
            if arr[nr][sc] != arr[sr][nc] :
                return 'no'
            else : cnt += 1
    return 'yes'

def check_square(sr,sc) :
    global cnt
    for i in range(cnt) :
        for j in range(cnt) :
            if arr[i][j] != '#' :
                return 'no'
    return 'yes'
        


T = int(input())
for tc in range(1,T+1) :
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    cnt = 1             # 변의 길이. 시작점을 포함하므로 1
    result = 'yes'

    for r in range(N) :
        for c in range(N) :
            # 좌우 길이 확인
            if arr[r][c] == '#' :
                result = check_len(r,c)
                if result != 'no' :
                    result = check_square(r,c)

    print(f'#{tc} {result}')
                
                
                
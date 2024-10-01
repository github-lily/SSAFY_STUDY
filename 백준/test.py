import sys
sys.stdin = open("C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt")

'''
- RxC 크기의 격자판
- 공기청정기는 항상 1번 열에 설치, 크기는 두 행을 차지
- 1초동안 미세먼지가 있는 모든 칸에서 동시에 인접한 네방향으로 확산이 일어남
- 확산되는 양 : 기존값//5
- 남은 양 : 기존값 - (확산되는양 x 확산된 칸의 개수)
- 그 뒤 공기청정기가 작동한다(위는 반시계방향, 아래는 시계방향)
- 미세먼지는 바람 방향으로 한 칸씩 이동하고, 공기청정기로 들어간 미세먼지는 모두 정화된다

- 입력값 : R,C,T(시간), 배열
- 출력값 : 방에 남아있는 미세먼지의 양
'''

'''
1. 공기청정기 위치 탐색
2. 미세먼지 확산
3. 공기청정기 가동
4. 반복 끝난 후 합계 구하기
'''

T = int(input())
for tc in range(1,T+1) :
    R, C, T = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(R)]

    # 확산에 사용할 델타 리스트
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    # T초 동안 반복
    for _ in range(T) :
        # 1. 공기청정기 위치 탐색
        for r in range(R) :
            if arr[r][0] == -1 :
                air1, air2 = r, r+1         # 공기청정기 위치 저장
                arr[r][0] = arr[r][1] = 0   # 계산 편의를 위해 0으로 설정
                break

        # 2. 미세먼지 확산
        # 확산이 "동시에" 발생하므로 임시 배열 temp 생성
        temp = [x[:] for x in arr]
        for r in range(R) :
            for c in range(C) :
                if arr[r][c] > 4:       # 5보다 작으면 몫이 0이므로 확산이 일어나지 않음
                    t = arr[r][c]//5
                    for i in range(4) :
                        nr, nc = r + dr[i], c + dc[i]
                        if 0 <= nr < R and 0<= nc <C :
                            temp[r][c] -= t
                            temp[nr][nc] += t

        # 확산 된 값을 원래 배열에 저장
        arr = temp

        # 3. 공기청정기 작동
        # 값을 덮어씌워야 하므로 바람이 부는 방향의 반대로 계산하기
        # 목적지 기준(덮어쓰여질 곳 기준)
        #위
        for i in range(air1-1,0,-1) :
            arr[i][0] = arr[i-1][0]
        for j in range(0, C-1, 1) :
            arr[0][j] = arr[0][j+1]
        for i in range(0,air1,1) :
            arr[i][C-1] = arr[i+1][C-1]
        for j in range(C-1,0,-1) :
            arr[air1][j] = arr[air1][j-1]
        
        # 아래
        for i in range(air2+1,R-1,1) :
            arr[i][0] = arr[i+1][0]
        for j in range(0,C-1,1) :
            arr[R-1][j] = arr[R-1][j+1]
        for i in range(R-1,air2,-1) :
            arr[i][C-1] = arr[i-1][C-1]
        for j in range(C-1,0,-1) :
            arr[air2][j] = arr[air2][j-1]


    # 답 구하기
    ans = sum(map(sum,arr))
    print(f'{tc} {ans}')




        # for i in range(air1-1,0,-1) :
    #     arr[i][0] = arr[i-1][0]
    # for j in range(0, C-1, 1) :
    #     arr[0][j] = arr[0][j+1]
    # for i in range(0,air1,1) :
    #     arr[i][C-1] = arr[i+1][C-1]
    # for j in range(C-2,0,-1) :
    #     arr[air1][j] = arr[air1][j-1]
    
    # # 아래
    # for i in range(air2+1,R,1) :
    #     arr[i][0] = arr[i-1][0]
    # for j in range(1,C,1) :
    #     arr[R-1][j] = arr[R-1][j-1]
    # for i in range(R-2,air2-1,-1) :
    #     arr[i][C-1] = arr[i+1][C-1]
    # for j in range(C-2,0,-1) :
    #     arr[air2][j] = arr[air2][j+1]
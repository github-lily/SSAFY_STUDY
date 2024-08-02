for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    arr_rvs = arr[::-1]  # 2를 시작으로 생각하기
    start = 0  # 진행되는 y좌표값
    for i in range(100):  # 첫 시작 좌표 찾기
        if arr_rvs[0][i] == 2:
            start = i

    for i in range(99, -1, -1):
        right = start + 1  # 오른쪽 좌표
        left = start - 1  # 왼쪽 좌표
        if  right < 100 and arr_rvs[i][right] == 1:
            for r in range(right, 100):  # 0이 나오기 직전 좌표값 찾기
                if arr_rvs[i][r] == 0:
                    break
                start = r
        elif 0 <= left  and arr_rvs[i][left] == 1:
            for l in range(left, -1, -1): # 98부터 0까지
                if arr_rvs[i][l] == 0:
                    break
                start = l
    print(f'#{tc} {start}')
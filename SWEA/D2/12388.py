'''
1. 너비만큼 칠함
2. 왼쪽 위 인덱스, 오른쪽 아래 인덱스, 칠할 색상(1 빨강, 2 파랑)
    칠해질 때마다 +1
3. 빨강과 파랑이 겹치는 부분의 크기
    겹치는 부분은 값이 2!
'''

T = int(input())

for tc in range(1,T+1):
    cnt = 0
    N = int(input())    #칠할 영역의 개수
    arr = [[0] * 10 for _ in range(10)]  # NxN 박스
    for k in range(N):
        r1k,c1k,r2k,c2k,color = list(map(int,input().split()))
         # r1, c1 : 첫번째 색칠 시작점 #r2, c2 : 첫번째 색칠 끝나는 점

        for i in range(r1k, r2k+1) :
            for j in range(c1k, c2k+1) :
                arr[i][j] += 1
                if arr[i][j] == 2:
                    cnt += 1

    # for lst in arr :
    #     print(*lst)
    #     print()



    print(f'#{tc} {cnt}')



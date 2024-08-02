import sys
sys.stdin = open("1210.txt", "r")

for _ in range(10) :
    #99번행에서의 2의 위치를 찾기
    tc = input()
    arr = [list(map(int,input().split())) for _ in range(100)]
    r=c=0
    for i in range(100) :
        if arr[99][i] == 2 :
            r,c = 99, i
            break



    while r>0 :
        # 현재(r,c)에서 이동
        arr[r][c] = 0 #좌우 무한루프에 빠지지 않도록 지나온 길의 값을 0으로 바꿈
        #왼쪽 #감소하는 것이니 상한은 안둬도 됨. c>0과 같음
        if c -1 >= 0 and arr[r][c-1] == 1:      #범위를 벗어나지 않고, 1이면
            while c -1 >= 0 and arr[r][c-1] == 1:     #왼쪽 끝까지 이동
                c -= 1 #왼쪽으로 이동
            r -= 1     #다시 오른쪽으로 가지 않도록 위로 한 칸 올림
        #오른쪽
        elif c+1<100 and arr[r][c + 1] == 1:
            while c < 99 and arr[r][c+1] == 1:
                c += 1 #오른쪽으로 이동, while로 반복
            r -= 1
        #위로 #좌우에 길이 없으면 위로 이동
        else :
            r -= 1
    print(f'#{tc} {c}')

    #더 간단히
    '''
    while r>0 :
        # 현재(r,c)에서 이동
        arr[r][c] = 0 #좌우 무한루프에 빠지지 않도록 지나온 길의 값을 0으로 바꿈
        #왼쪽 #감소하는 것이니 상한은 안둬도 됨. c>0과 같음
        if c -1 >= 0 and arr[r][c-1] == 1:      #범위를 벗어나지 않고, 1이면
            while c -1 >= 0 and arr[r][c-1] == 1:     #왼쪽 끝까지 이동
                c -= 1 #왼쪽으로 이동
        #오른쪽
        elif c+1<100 and arr[r][c + 1] == 1:
            while c < 99 and arr[r][c+1] == 1:
                c += 1 #오른쪽으로 이동, while로 반복
        #위로 
        r -= 1      #무조건 이동 후 위로 올라가도록!
    print(c)
    '''
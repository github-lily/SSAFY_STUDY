import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt')

''' 진행 순서
1. 낚시꾼의 열 이동
2. 상어 낚시(제거)
3. 상어 이동
4. 겹치는 상어 제거
'''

R,C,M = map(int,input().split())
info = [list(map(int,input().split())) for _ in range(M)]
ans = 0     # 상어 크기의 합

# 상어 정보를 담은 배열
# [0][1] : 상어의 위치, [2] : 속도, [3] : 방향, [4] : 크기
# 행, 열, 크기 순으로 정렬(오름차순) -> 땅(0번행)에 가깝고 크기가 작은 물고기가 위로가게
info.sort(key=lambda x : (x[0],x[1],x[4]))

# 이동 방향 리스트(상하우좌)
dr,dc = [0,-1,1,0,0],[0,0,0,1,-1]

# 방향 전환 리스트(상하우좌, 역방향)
reverse = [0,2,1,4,3]

#낚시꾼의 열 이동, 상어 낚시
k = 0   #낚시꾼의 위치
while k < R :
    for i in range(R) :
        if info[i][1] == k :        # 낚시꾼과 같은 위치라면
            ans += info[i][4]       # 상어 크기 더해주기
            info.pop(i)             # 낚시한 상어 제거
            break
    
    # 상어 이동
    
    for n in range(len(info)) :


        # 잘못된 코드1 : 속도가 (R-1)*2 or (C-1)*2 보다 큰 수의 경우 오류가 남

        # # 방향, 속도만큼 행과 열 이동
        # info[n][0] += dr[info[n][3]] * info[n][2]       # 행
        # info[n][1] += dc[info[n][3]] * info[n][2]       # 열

        # if info[n][0] < 0 :     # 위쪽으로 벗어남
        #     info[n][0] += R
            # info[n][3] = reverse[info[n][3]]    # 방향 전환
        # if info[n][0] > R-1 :   # 아래쪽으로 벗어남
        #     info[n][0] -= R
        #     info[n][3] = reverse[info[n][3]]
        # if info[n][1] < 0 :     # 왼쪽으로 벗어남
        #     info[n][1]      # 모르겠음
        #     info[n][3] = reverse[info[n][3]]
        # if info[n][1] > C-1 :   # 오른쪽으로 벗어남
        #     info[n][1]      # 모르겠음
        #     info[n][3] = reverse[info[n][3]]

        # 잘못된 코드2 : 기존값+이동값이 범위를 벗어날 수 있음
        # 상하일때
        # if info[n][3] == 1 or info[n][3] == 2 :
        #     info[n][0] += (info[n][2]%R)

        # # 좌우일때
        # else :          # if info[n][3] == 3 or info[n][3] == 4 :
        #     info[n][1] += (info[n][2]%C)        


        # info[n][3] = reverse[info[n][3]]    # 방향 전환



    
    # 같은 위치 걸러주기
    r = 1
    while r < len(info) :
        if info[r-1][0:2] == info[r][0:2] :
            info.pop(r-1)           # 크기가 작은 상어 제거
        else :
            r+1    
    
    # 낚시꾼 위치 이동
    k += 1 
        
    
print(ans)
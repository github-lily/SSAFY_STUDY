import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/portfolio/백준/test.txt')


R,C,M = map(int,input().split())
shark = []
ans = 0
for _ in range(M) :
    i,j,s,d,z = list(map(int,input().split()))
    shark.append([i-1,j-1,s,d,z])       # i,j 좌표를 0부터 시작하게 저장


W,H = 2*C-2, 2*R-2      #반복되는 구간 설정
# 구간 테이블 설정
wtbl = [n for n in range(C)] + [n for n in range(C-2,0,-1)]
htbl = [n for n in range(R)] + [n for n in range(R-2,0,-1)]
opp = {1:2, 2:1, 3:4, 4:3}      # 방향 전환 dict

# 1. j열의 가장 위 상어를 잡기(j열에서 처음 만난 상어)
#[0] : i, [1] : j, [2] : speed, [3] : 방향, [4] 크기
for fisher in range(C) : # 0열~C-1열까지 처리
    
    # 열, 행 오름차순 정렬
    shark.sort(key=lambda x : (x[1],x[0]))  

    for i in range(len(shark)) : # 잡으면 사라지니 len으로
        if shark[i][1] == fisher :
            ans += shark[i][4]
            shark.pop(i)
            break
                
    # 2. 상어 이동
    for i in range(len(shark)) :
        #좌우방향으로 움직일 경우
        if shark[i][3] >= 3 :
            dr = 1 if shark[i][3] == 3 else -1          # 우측이면 1, 좌측이면 -1
            shark[i][1] = (shark[i][1] + shark[i][2] *dr) % W
            if C <= shark[i][1] :
                shark[i][1] = wtbl[shark[i][1]]         # 좌표 변환
                shark[i][3] = opp[shark[i][3]]          # 방향 반대

        # 상하로 움직일 경우
        else :
            dr = 1 if shark[i][3] == 2 else -1          # 아래면 1, 위면 -1
            shark[i][0] = (shark[i][0] + shark[i][2] *dr) % H
            if R <= shark[i][0] :
                shark[i][0] = htbl[shark[i][0]]         # 좌표 변환
                shark[i][3] = opp[shark[i][3]]          # 방향 반대

    # 3. 상어 정렬 후 아래서부터 작은 상어가 같은 좌표면 삭제
    # 행과 열은 오름차순, 크기는 내림차순으로 정렬
    shark.sort(key=lambda x : (x[1],x[0],-x[4])) 
    # 가장 끝에서 1번까지 처리
    for i in range(len(shark)-1,0,-1) :
        # 위의 상어가 나의 좌표와 같다면 나를 삭제 (크기 내림차순이니까)
        if (shark[i][0:2]) == (shark[i-1][0:2]) :
            shark.pop(i)

        
print(ans)
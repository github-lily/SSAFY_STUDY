import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt')



# 비교하며 다시 칠해줄 함수
def reapaint_cnt(temp, chess) :
    cnt = 0
    for i in range(8) :
        for j in range(8) :
            if temp[i][j] != chess[i][j] :
                # temp[i][j] = chess[i][j]        
                # 값을 바꾸면 원본도 바뀌어 정확한 비교가 안됨!
                cnt += 1
    return cnt


M,N = map(int,input().split())
arr = [input() for _ in range(N)]
ans = 99999999999999999999999999999999999999999999999




# 시작의 2가지 경우를 정의
W_start = ['WBWBWBWB','BWBWBWBW'] *4
B_start = ['BWBWBWBW','WBWBWBWB'] *4


# 8x8을 만들 수 있는 범위만 돌기 (N-8+1)
for r in range(N-7) :
    for c in range(M-7) :
        # 임시 보드판 가져오기
        temp = [row[c:c+8] for row in arr[r:r+8]]
        W_start_cnt = reapaint_cnt(temp,W_start)
        B_start_cnt = reapaint_cnt(temp,B_start)
        ans = min(W_start_cnt,B_start_cnt,ans)

print(ans)
import sys
sys.stdin = open("백준/test.txt")

def find(H,W,N) :
    cnt = 0
    for j in range(W) :
        for i in range(H) :
            cnt += 1
            if cnt == N :
                room = (i+1)*100 + (j+1)
                print(room)
                return



import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    h,w,n = map(int,input().split())

    find(h,w,n)



# 높이는 상관 없음 무조건 엘베에서 가까운 방 선호
# 거리가 같을 경우 낮은 방 선호





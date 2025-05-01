import sys
sys.stdin = open("백준/test.txt")


import sys
input = sys.stdin.readline

R,C = map(int,input().strip().split())
arr = [list(input().strip()) for _ in range(R)]

max_cnt = 1
di, dj = [0,1,0,-1],[1,0,-1,0]


# 알파벳 방문 배열
dict = {'A':0,'B':0,'C':0,'D':0,'E':0,
        'F':0,'G':0,'H':0,'I':0,'J':0,
        'K':0,'L':0,'M':0,'N':0,'O':0,
        'P':0,'Q':0,'R':0,'S':0,'T':0,
        'U':0,'V':0,'W':0,'X':0,'Y':0,
        'Z':0}


def find(i,j,cnt) :
    global max_cnt

    if cnt > max_cnt :
        max_cnt = cnt

    for k in range(4) :
        ni, nj = i+di[k], j+dj[k]
        if 0 <= ni < R and 0 <= nj < C :        # 범위 내   
            if dict[arr[ni][nj]] == 0 :
                dict[arr[ni][nj]] = 1

                # 다음으로 진행
                find(ni,nj,cnt+1)

                # 초기화
                dict[arr[ni][nj]] = 0

dict[arr[0][0]] = 1
find(0,0,1)     # 처음 지점도 포함
print(max_cnt)



            



# # 지수 찾는 함수
# def find(i,esp) :
    
#     while True :
#         if i < 2**esp :
#             return esp-1
#         esp += 1
    

# def check(n,m) :
#     # 지수 찾기
#     x = find(n,0)
#     y = find(m,0)

#     # 지수 그룹이 달라질때까지 계산
#     while True : 
#         # 지수 그룹이 다르면 큰 지수 그룹 
#         if x != y:
#             ans = max(x,y)
#             return ans
        
#         # 지수 그룹이 같으면 지수 그룹이 달라질때까지 계산 
#         else :
#             n = n - (2**(x-1))
#             m = m - (2**(x-1))
#             x = find(n,0)
#             y = find(m,0)

# length, n, m = map(int,input().split())

# ans = check(n,m)
# print(ans)

import sys
sys.stdin = open("백준/test.txt")

chess = [list(input()) for _ in range(8)]


# 하얀칸
# i가 짝수일 때 j도 짝수인 곳
# i가 홀수일 때 j도 홀수인 곳
ans = 0

for i in range(8) :
    for j in range(8) :
        is_odd_j = j % 2
        # 짝수일 때
        if i % 2 == 0 :
            if is_odd_j == 0 and chess[i][j] == "F" :
                ans += 1
        # 홀수일 때
        else :
            if is_odd_j == 1 and chess[i][j] == "F" :
                ans += 1

print(ans)
             



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

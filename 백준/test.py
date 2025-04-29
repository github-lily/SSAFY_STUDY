import sys
sys.stdin = open("백준/test.txt")

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    result = input().strip() 
    N = len(result)

    final_score = 0
    score = 0

    for mark in result :
        if mark == 'O' :
            score += 1
            final_score += score

        else :
            score = 0

    print(final_score)


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

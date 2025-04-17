import sys
sys.stdin = open("백준/test.txt")

N = int(input())


# 5로 나누어떨어질 때
if N % 5  == 0 :
    print(N//5)

else :
    p = 0
    while N > 0 :
        N -= 3
        p += 1
        # 3과 5를 조합할 때
        if N % 5 == 0 :
            p += N//5
            print(p)
            break
        
        # 3과 5로 나눌 수 없을 때
        elif N == 1 or N == 2 :
            print(-1)
            break

        # 3으로 나누어 떨어질 때
        elif N == 0 :
            print(p)
            break

    





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

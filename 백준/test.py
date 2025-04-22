import sys
sys.stdin = open("백준/test.txt")

N, M = map(int,input().split())

poketmons_num = {}      # key = 포켓몬 번호
poketmons_name = {}     # key = 포켓몬 이름

for i in range(1,N+1) :
    name = input()
    poketmons_num[i] = name
    poketmons_name[name] = i

for _ in range(M) :
    q = input()
    if q.isdigit() :    # 숫자로만 되어있다면
        # print(q)
        print(poketmons_num[int(q)])
    else :
        print(poketmons_name[q])



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

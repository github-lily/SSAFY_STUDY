import sys
sys.stdin = open("백준/test.txt")

n = int(input())
player_list = []
result = []

for _ in range(n):
    a = input()
    player_list.append(a[0])

first_names = set(player_list)

for i in first_names:
    if player_list.count(i) >= 5:
        result.append(i)

if len(result) > 0:
    print(''.join(sorted(result)))
else:
    print("PREDAJA")

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

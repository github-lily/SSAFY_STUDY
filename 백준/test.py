import sys
sys.stdin = open("백준/test.txt")

N = int(input())

temp = list(map(int,input().split()))

# lst = []
# for i in range(1,N+1) :
#     lst.append((i,temp[i-1]))

# num = 0
# ans = []
# while lst :
#     order =lst.pop(num)
#     print(order)
    
order_lst = []
num = 0

while temp :
    order_lst.append(num+1)
    temp_num = temp.pop(num)
    num += temp_num

print(order_lst)
    





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

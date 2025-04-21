import sys
sys.stdin = open("백준/test.txt")


N = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0

# B 인덱스와 함께 값 저장
idx_B = []

for i in range(N) :
    idx_B.append((B[i],i))

# B 오름차순 정렬
idx_B.sort(key=lambda x:x[0])


# A  내림차순 정렬(그리디)
A.sort(reverse=True)



for idx in range(N) :
    ans += A[idx] * idx_B[idx][0]

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

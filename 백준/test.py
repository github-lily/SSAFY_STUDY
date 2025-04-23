import sys
sys.stdin = open("백준/test.txt")



while True :
    # 길이값 오름차순 정렬렬
    length = sorted(map(int,input().split()))

    if sum(length) == 0 :
        break

    a = length[0]
    b = length[1]
    c = length[2]

    # 분기
    if a == b == c :
        print("Equilateral")
    elif a + b <= c :
        print("Invalid")
    elif a == b != c or a != b == c or a == c != b :
        print("Isosceles")
    else :
        print("Scalene")




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

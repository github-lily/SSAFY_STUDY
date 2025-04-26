import sys
sys.stdin = open("백준/test.txt")

order = list(map(int,input().split()))

flag = 3        # 시작

for i in range(1, 8) :
    # 1씩 증가할 때
    if order[i-1] + 1 == order[i] :
        if flag == 0 :      # 이전에는 감소했다면 mixed
            print("mixed")
            break
        else :
            flag = 1        # 증가하면 flag = 1
    # 1씩 감소할 때
    elif order[i-1] - 1 == order[i] :
        if flag == 1 :      # 이전에는 증가했다면 mixed
            print("mixed")
            break
        else :
            flag = 0        # 감소하면 flag = 0
    # 1씩 증가하거나 감소하지 않을 때때
    else :
        print("mixed")
        flag = 2
        break      

# 끝까지 순서대로 증가/감소를 확인하면 출력
if flag == 1 :
    print("ascending")
elif flag == 0 :
    print("descending")


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

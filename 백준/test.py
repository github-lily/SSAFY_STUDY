import sys
sys.stdin = open("백준/test.txt")

N = int(input())
ans = 0
for _ in range(N) :
    text = input()
    n = len(text)

    # 한 글자인 경우
    if n == 1 :
        ans += 1

 
    # 한 글자 이상인 경우
    else :
        t_set = set(text[0])
        flag = True
        for i in range(1, len(text)) :
            if text[i] in t_set :               # 중복된 수가 나왔을 때
                if text[i-1] != text[i] :       # 이전값과 다르다면 중단
                    flag = False
                    break
            else :
                t_set.add(text[i])
        if flag == True :
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

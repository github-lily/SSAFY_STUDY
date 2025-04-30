import sys
sys.stdin = open("백준/test.txt")


import sys
input = sys.stdin.readline




N = int(input())
stack = []
for _ in range(N) :
    cmd = input().strip().split()

    # push 인 경우
    if len(cmd) == 2 :
        stack.append(cmd[1])
    else :
        text = cmd[0]
        if text == "pop" :
            if stack :
                print(stack.pop())
            else :
                print(-1)    
        
        elif text == "size" :
            print(len(stack))
        
        elif text == "empty" :
            if stack :
                print(0)
            else :
                print(1)
        else :
            if stack :
                print(stack[-1])
            else :
                print(-1)
            



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

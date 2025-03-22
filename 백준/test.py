import sys
sys.stdin = open('백준/test.txt')

# def check() :
#     global N, depth

#     num_lst = []
#     while N // 2 > 1 :
#         if N % 2 == 0 :     # 짝수라면
#             for i in range(1, (N//2)+1) :
#                 if (i == user1 and i+1 == user2) or (i == user2 and i+1 == user1) :
#                     print(depth)
#                     return
#                 elif i+1 == user1 or i+1 == user2 :
#                     num_lst.append(i+1)
#                 else :
#                     num_lst.append(i)

#         else :              # 홀수라면
#             for i in range(1, (N//2)+1) :
#                 if (i == user1 and i+1 == user2) or (i == user2 and i+1 == user1) :
#                     print(depth)
#                     return
#                 elif i+1 == user1 or i+1 == user2 :
#                     num_lst.append(i+1)
#                 else :
#                     num_lst.append(i)
            


# # 리스트의 길이 N
# N, user1, user2 = map(int,input().split())

# depth = 1
# lst = [x for x in range(1,N+1)]

# while 
#     for i in range(1, (N//2)+1) :
#         if (i == user1 and i+1 == user2) or (i == user2 and i+1 == user1) :
#             print(depth)
#             return
    

# 리스트의 길이 N
N, user1, user2 = map(int,input().split())


lst = []
depth = 1
for i in range(1,N+1) :
    # 답인 경우
    if (i == user1 and i+1 == user2) or (i == user2 and i+1 == user1) :
        print(depth)
        break
    
    # i+1이 user1 또는 user2인 경우
    elif i+1 == user1 :
        lst.append(i+1)
        user1 == lst[n]
        
    
    else :
        lst.append(i)
    
    depth += 1
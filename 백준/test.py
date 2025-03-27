import sys
sys.stdin = open("백준/test.txt")

import sys
from collections import Counter

word = sys.stdin.readline().strip().upper()  # 대문자로 변환
counter = Counter(word)  # 알파벳 개수 세기

max_count = max(counter.values())  # 가장 많이 등장한 횟수 찾기
most_common = [char for char, count in counter.items() if count == max_count]  # 최다 빈도 문자 찾기

# 최다 빈도 문자가 하나면 출력, 여러 개면 '?'
print(most_common[0] if len(most_common) == 1 else '?')


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

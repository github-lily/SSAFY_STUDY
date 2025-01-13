import sys
sys.stdin = open('백준/test.txt')

a = int(input())
b = int(input())
c = int(input())

print(a+b-c)
print(int(str(a)+str(b))-c)

# n = int(input())
# arr = [list(map(int,input().split())) for _ in range(n)]


# dp = [0] * n

# floor = n

# while floor > 0 :
#     for i in range(n) :
#         for j in range()
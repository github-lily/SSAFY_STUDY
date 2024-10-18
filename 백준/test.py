import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt')

2588




# A = int(input())
# B = input()

# C = A * int(B[2])
# D = A * int(B[1])
# E = A * int(B[0])
# b = int(B)
# ans = A * b


# print(C)
# print(D)
# print(E)
# print(ans)



a=int(input())
b=input()
for i in range(1,4):
    print(a*int(b[-i]))
print(a*int(b))
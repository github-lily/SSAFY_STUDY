import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/portfolio/백준/test.txt')


A,B,C = map(int,input().split())


a,b = map(int,input().split())

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)
       

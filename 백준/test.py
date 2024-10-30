import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/portfolio/백준/test.txt')

max_v = 0
max_idx = 0
for i in range(1,10) :
    num = int(input())
    if num > max_v :
        max_v = num
        max_idx = i

print(max_v)
print(max_idx)
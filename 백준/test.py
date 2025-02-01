import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())


N = int(input())
sum_val = 0

for i in range(N+1) :
    sum_val += i

print(sum_val)
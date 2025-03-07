import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())
N = int(input())
F = int(input())

# 마지막 두 자리를 00으로 변경
N = (N // 100) * 100

# F로 나누어떨어지는 가장 작은 수 찾기
while N % F != 0:
    N += 1

# 마지막 두 자리만 출력
print(str(N)[-2:])

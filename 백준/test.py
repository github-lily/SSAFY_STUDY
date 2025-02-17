import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())
import sys

# 입력 받기
N = int(input())
num_stack = []
for _ in range(N) :
    num = input()

    if num == '0' :
        num_stack.pop()
    else :
        num_stack.append(num)

print(sum(map(int, num_stack)))

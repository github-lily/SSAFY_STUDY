import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())
import sys
import math

# 입력 받기
T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    # 조합 계산: M개 중 N개를 선택하는 경우의 수
    result = math.comb(M, N)  # math.comb(M, N) == M! / (N! * (M-N)!)
    print(result)

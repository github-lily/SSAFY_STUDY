import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())
# 체스 말의 기본 개수
standard = [1, 1, 2, 2, 2, 8]

# 입력값을 리스트로 변환
input_pieces = list(map(int, input().split()))

# 각 체스 말의 부족하거나 남은 개수 계산 후 출력
result = [standard[i] - input_pieces[i] for i in range(6)]

# 결과 출력
print(*result)

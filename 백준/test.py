import sys
sys.stdin = open('백준/test.txt')


# 영수증의 총 금액
X = int(input())

# 구매한 물건의 종류 수
N = int(input())

# 물건들의 총합 계산
total = 0
for _ in range(N):
    a, b = map(int, input().split())
    total += a * b

# 결과 출력
if total == X:
    print("Yes")
else:
    print("No")

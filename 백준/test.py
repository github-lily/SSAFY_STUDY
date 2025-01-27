import sys
sys.stdin = open('백준/test.txt')

N = int(sys.stdin.readline().strip())


# 위쪽 삼각형 출력
for i in range(1, N + 1):
    spaces = ' ' * (N - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)

# 아래쪽 삼각형 출력
for i in range(N - 1, 0, -1):
    spaces = ' ' * (N - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)

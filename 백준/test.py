import sys
sys.stdin = open('백준/test.txt')


N = reversed(sorted(list(input())))
ans = ''.join(N)
print(ans)

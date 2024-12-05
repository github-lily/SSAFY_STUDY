import sys
sys.stdin = open('백준/test.txt')


data = sys.stdin.read()


N = int(input())
card = list(map(int,input().split()))
M = int(input())
have = list(map(int,input().split()))

cnt = [0] * 500001
for number in card :
    cnt[number] += 1


ans = [cnt[num] for num in have]
print(*ans)
import sys
sys.stdin = open('백준/test.txt')

N = int(input())

shirts = list(map(int,input().split()))
T, P = map(int,input().split())

# 구매해야하는 개수
t = 0


for size in shirts :
    moc = size // T
    remain = size % T

    if remain == 0 :
        t += moc
    else :      # 나머지가 있다면 한세트 추가
        t += (moc + 1)


p_set = N // P
p_each = N % P

print(t)
print(p_set, p_each)
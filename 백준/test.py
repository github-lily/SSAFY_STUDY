import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())

N,K = map(int,input().split())

ans = []
for i in range(1,N+1) :
    rest = N % i
    if rest == 0 :
        if i not in ans :
            ans.append(i)
if len(ans) < K :
    print(0)
else :
    print(sorted(ans)[K-1])



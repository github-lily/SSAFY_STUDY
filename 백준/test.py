import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt')



N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ans_lst = []

for _ in range(M) :
    sr,sc,er,ec = map(int,input().split())
    sr,sc,er,ec = sr-1,sc-1,er-1,ec-1       # 인덱스 맞춰주기
    sum_val = 0                             # 구간합

    for r in range(sr,er+1) :
        for c in range(sc,ec+1) :
            sum_val += arr[r][c]
    ans_lst.append(sum_val)


for ans in ans_lst :
    print(ans)



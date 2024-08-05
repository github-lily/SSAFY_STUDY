# 수정


for tc in range(1,11) :
    tc = int(input())
    t = input()     #text
    p = input()     #pattern
    
    n = len(t)
    m = len(p)

    cnt = s = 0
    while s <= n-m :
        found = True
        # for s in range(n-m+1) : #s 범위 위에서 지정해주니까 따로 할 필요 없음
        for i in range(m) :
            if p[i] != t[s+i] :
                found = False
                break       #안맞으면 멈춤, 맞으면 끝까지 돈다
        if found:
            cnt += 1
            s = s + m-1     #시작위치를 m 다음 인덱스로 이동, +1 있으니 -1
        s += 1              #찾던 못찾던 다음으로 넘어갈 수 있게 +1
    print(f'#{tc} {cnt}')
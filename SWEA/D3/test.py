import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/SWEA/D3/test.txt')




def bfs(s) :
    # 1. q, v 생성
    q = []
    v = [0] * 101

    # 2. q,v 삽입
    q.append(s)
    v[s] = 1
    ans = s         #리턴할 값, 아무도 연결 안되어있으면 자기자신

    # 3. 탐색
    while q :
        c = q.pop(0)
        if v[c] > v[ans] or (v[c] == v[ans] and c > ans) :
            ans = c

        for n in lst[c] :
            if v[n] == 0 :
                q.append(n)
                v[n] = v[c]+1


    return ans




for tc in range(1,11) :
    N, S = map(int,input().split())
    phone = list(map(int,input().split()))
    lst = [[] for _ in range(101)]


    for i in range(0,len(phone),2) :
        s,e = phone[i], phone[i+1]
        lst[s].append(e)

    ans = bfs(S)
    print(f'#{tc} {ans}')
    
    
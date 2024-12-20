import sys
sys.stdin = open('백준/test.txt')


from collections import deque



def find(start,end) :

    q = deque()
    v = [0]*200001

    q.append(start)
    v[start] = 1

    while q :
        cn = q.popleft()

        if cn == end :
            return v[cn]-1
        
        for w in (2*cn, cn-1, cn+1) :
            if 0<= w < 200000 :        # 범위 내
                if v[w] ==0 :
                    v[w] = v[cn] +1
                    q.append(w)
                    
    return -1       # 디버깅용용


N,K = map(int,input().split())


ans = find(N,K)
print(ans)
import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt')


from collections  import deque

def bfs(s,e) :        # 시작노드 s
    q = deque()
    v = [0] * (N+1)

    q.append(s)
    v[s] = 1

    while q:
        c = q.popleft()
        if c == e :
            return v[c]-1 

        for w in friends[c] :
            if v[w] == 0 :
                q.append(w)
                v[w] = v[c] + 1




# 노드의 개수(N) 입력 받음
N = int(input())

# 최단경로 리스트 생성
arr = [[0]*(N+1) for _ in range(N+1)]

# 본인-> 본인 경로는 0으로 셋팅
for a in range(N+1) :
    for b in range(N+1) :
        if a == b :
            arr[a][b] = 0

# 연결관계 입력받기
friends = [[]*(N+1) for _ in range(N+1)]

while True :
    a,b = map(int,input().split())
    if a+b == -2 :
        break 
    friends[a].append(b)
    friends[b].append(a)


for start in range(1,N) :
    for end in range(start, N+1) :
        cost = bfs(start,end)       # 노드마다 s->e 점수 구하기
        arr[start][end] = cost
        arr[end][start] = cost      # 양방향이므로 번갈아서 저장


# 최대점수 저장
max_val = [0] * (N+1)
for k in range(1,N+1) :
    max_val[k] = max(arr[k])


min_val = min(max_val[1:])      # 0번 인덱스는 무효값이므로 1번부터 (안그러면 0이 최소)

# 최소값과 같은 후보자를 후보자 리스트에 저장
candidate = []
for i in range(N+1) :
    if max_val[i] == min_val :
        candidate.append(i)


# 오름 차순으로 정렬
candidate = sorted(candidate)


# 최소 점수, 후보 수
# 후보자
print(f'{min_val} {len(candidate)}')
print(*candidate)

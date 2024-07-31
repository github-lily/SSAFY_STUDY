data = [0,4,1,3,1,2,4,1]
counts = [0]*5          # data가 0~4까지의 정수

N = len(data)           # data의 크기
temp = [0] * N          # 정렬 결과 저장

# 1단계 : data 원소 별 개수 세기

for x in data :
    counts[x] +=1       # data 의 원소 x를 가져와서 counts[x]에 개수 기록


# 2단계 : 각 숫자까지의 누적 개수 구하기
for i in range(1,5):    # counts[1]~counts[4]까지 누적 개수
    counts[i] = counts[i-1] + counts[i]


# 3단계 :
for i in range(N-1, -1, -1) :       # N-1부터 0까지 (N-1 이하, -1 초과) 거꾸로(-1)
    counts[data[i]] -= 1            # 누적개수 1개 감소
    temp[counts[data[i]]] = data[i]

print(*temp)
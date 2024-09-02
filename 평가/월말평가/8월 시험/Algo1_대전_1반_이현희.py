

'''
- N개의 활동 구역
- 먹이를 먹으면 K칸만큼 더 이동
- 추가로 먹이를 못 먹으면 K번째 칸에서 멈춤
- 마생물이 최대 몇 번째 칸까지 이동할 수 있는지 알아내는 프로그램
- 먹이가 있으면 1, 없으면 0
- 첫번째 구역에는 항상 먹이가 있음
- 1부터 N번까지 칸(인덱스 0~N-1)
'''


T = int(input())
for tc in range(1,T+1) :
    N, K = map(int,input().split())     #활동 구역의 범위 N , #먹이를 먹고 이동할 수 있는 칸 수 K
    feed = list(map(int,input().split()))   #경로의 먹이 정보

    power = K   #현재 갈 수 있는 칸 수, 첫번째 칸엔 무조건 먹이가 있으므로

    for i in range(1, N) :     #현재 위치 i
        power -= 1              #한 칸 이동했으니 힘 하나 뺌
        if i == N-1 :           #종착지에 도착하면
            ans = i+1           #인덱스랑 다르게 1부터 시작하니까 +1
            break               #중단

        elif feed[i] == 1 :       # 먹이가 있다면
            power = K           # 먹이를 먹으면 K칸만큼 더 이동(먹이 누적x)

        elif power == 0 :       # 힘이 없다면
            ans = i+1
            break               #중단

    print(f'#{tc} {ans}')
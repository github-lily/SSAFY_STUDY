
'''
길이 N
어떤 원소를 중심으로 한 가장 긴 대칭 구간의 길이를 알아내는 프로그램
중심원소를 포함(대칭구간의 길이는 항상 +1, 홀수)
대칭구간이 없는 경우 중심원소만임을 나타내는 1 출력
'''

'''
1. 전체 순회하며 대칭 비교

'''

T = int(input())
for tc in range(1,T+1) :
    N = int(input())                # 배열의 길이
    arr = list(map(int,input()))        # 2진수 # 인덱스 사용하기 위해 리스트로 받기

    ans = 1     #중심원소 하나 포함

    for i in range(1, N-1) :    #맨 처음과 맨 끝은 대칭원소가 없으므로 제외
        cnt = 1
        for j in range(1,N//2+1) :  #자기자신은 cnt값에 포함되므로 1부터 시작
            left = i-j
            right = i+j
            if i-j<0 or i+j >N-1 :     #범위 밖이라면 중단
                break

            if arr[left] == arr[right] :    #대칭이라면
                cnt += 2
                if ans < cnt :              #최대 대칭 개수 찾기
                    ans = cnt
            else :
                break                   #대칭이 아니라면 중단

    print(f'#{tc} {ans}')



# 다른 풀이법
# while left >= 0 and right < N and arr[left] != arr[right]
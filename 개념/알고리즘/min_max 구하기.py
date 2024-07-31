import sys
sys.stdin = open('min_max.txt')
# 파일에 저장된 값을 입력값으로 넣는 것
# 제출할 땐 삭제하거나 주석처리!  보안문제에 걸림

T = int(input())        #줄이 바뀌기 전까지 한 줄을 입력 받음
#tc 개수 만큼 반복해서 입력을 받는다.

for tc in range(1, T+1) :
    N = int(input())
    arr = list(map(int,input().split()))        #배열 : array 에서 따서 arr로 많이 지음

#max



    # 문제의 답을 계산하고 출력
    ans = max(arr) - min(arr)


    #답을 출력
    print(f'#{tc} {ans}')
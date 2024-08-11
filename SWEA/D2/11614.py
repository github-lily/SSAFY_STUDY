import sys

sys.stdin = open("test.txt", "r")

'''

1. N 명의 학생이 가위바위보가 그려진 N장의 카드를 나눠 갖는다.
    1) 가위 : 1, 바위 : 2, 보 : 3
    2) 같은 카드인 경우 번호가 작은 쪽이 승자
    3) 1, 2 : 2 / 2, 3: 3 / 1, 3 : 1

2. 전체를 두 개의 그룹으로 나눈다
3. 그룹의 승자끼리 카드를 비교한다
    1) 그룹 내부를 두 그룹으로 나눈다(i번부터j번까지 속한 그룹)
        - (i+j)//2 , (i+j)//2+1
    2) 각각의 그룹에서 1등을 가린다
    3) 각 1등을 비교해 최종 1등을 가린다

4. 이긴 사람이 최종 승자가 된다
5. 1등을 찾는 프로그램


1. 승자를 비교하는 함수를 만든다.
2. 그룹을 두개로 나눈다.
3. 함수를 적용하여 승자를 뽑는다!


B : -1, 2
A : 1, -2


val = A - B
if val == 1 or val == -2 :
    print('A')
elif val == -1 or val == 2:
    print('B')

'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    def winner(a,b) :       #인덱스 번호
        val = arr[a-1] - arr[b-1]       #인덱스가 1번부터 시작이니까
        if val == 1 or val == -2 :
            return a
        elif val == -1 or val == 2:
            return b


    def find_min(lst, s, e):
        if s == e:
            return lst[s]
        else:
            mid = s + e // 2
            l_mid = find_min(s, mid)
            if mid == s+1 :
                l_winner = winner(s,mid)

            r_mid = find_min(mid + 1, e)
            if e == mid+2 :
                r_winner = winner(mid+1,e)


            winner(l_winner,r_winner)

    result = find_min(arr,0,N)
    print(f'#{tc} {result}')
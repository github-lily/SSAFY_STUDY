'''
10
0 0 254 185 76 227 84 175 0 0
10
0 0 251 199 176 27 184 75 0 0
'''
#import sys
#sys.stdin = open('view.txt')

for i in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    '''
        0 0 254 185 76 227 84 175 0 0
        이면, 2번째 인덱스부터 검사 시작
        인덱스의 value가 양 얖보다 크면 => 해당 수 - 양 옆의 수들 중 가장 큰 수
        인덱스의 value값이 양 옆보다 모두 크지 않으면 => pass
    '''

    ans_sum = 0
    for i in range(2, N-2):
        if (arr[i] >= arr[i-1]) and (arr[i] >= arr[i-2]) and (arr[i] >= arr[i+1]) and (arr[i] >= arr[i+2]):
            ans_sum += arr[i] - max(arr[i - 1], arr[i - 2], arr[i + 1], arr[i + 2])

    print(ans_sum)
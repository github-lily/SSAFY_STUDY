import sys
sys.stdin = open('백준/test.txt')


import sys
input = sys.stdin.readline

M = int(input())
S = set()

# all_S = [x for x in range(1,21)]
# 속도를 위해 set으로 만듦

all_S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}


for _ in range(M) :
    request = input().split()

    if request[0] == 'all' :
        S = all_S

    elif request[0] == 'empty' :
        S = set()
    
    # 이 경우엔 무조건 request[1]이 존재함함
    else :
        if request[0] == 'add' :
            S.add(int(request[1]))

        elif request[0] == 'remove' :
            S.remove(int(request[1]))

        elif request[0] == 'check' :
            if int(request[1]) in S :
                print(1)
            else :
                print(0)

        elif request[0] == 'toggle' :
            if int(request[1]) in S :
                S.remove(int(request[1]))
            else :
                S.add(int(request[1]))




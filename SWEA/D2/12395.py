'''
# 문자열 글자수
- str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾는다
- 그 중 가장 많은 글자의 개수를 출력한다
'''
import sys
sys.stdin = open("12395.txt","r")


T = int(input())
for tc in range(1, T+1) :
    str1 = list(input())   #['P', 'V', 'X', 'Y']
    str2 = list(input())    #['E', 'G', 'G', 'O', 'P', 'S', 'V', 'X', 'Y', 'Y']
    N = len(str1)
    M = len(str2)

    max_cnt = 0  # 가장 많은 수 #각 char count를 비교한 뒤 최종값이 return되야 하므로 for문 밖에 위치!
    for idx_1 in range(N) :
        if str1[idx_1] in str2 :        #str2에 str1의 값이 있다면
            cnt = 0  # count
            for idx_2 in range(M) :         #str2에서 순회하며
                if str1[idx_1] == str2[idx_2] :
                    cnt += 1            #str1[idx_1]과 같은 값이 있으면 count +1
            if max_cnt < cnt :
                max_cnt = cnt



    print(f'#{tc} {max_cnt}')

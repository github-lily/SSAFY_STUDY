#홀수만 더하기
#10개의 수를 입력받아 홀수만 더한 값을 출력
#0 =< N =< 1000

T = int(input())        #테스트 케이스의 개수 T
for t in range(1,T+1) :
    val = list(map(int,input().split()))

    odd_sum = 0
    for i in range(10) :
        if val[i] % 2 == 1 :
            odd_sum = odd_sum + val[i]
    print(f'#{t} {odd_sum}')

# print(a)
'''
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1 
'''


# my_list = [1,2,3,4,5,6,7,8,9]

# odd = []
# for i in range(len(my_list)) :
#     if my_list[i] % 2 == 1 :
#         odd.append(my_list[i])
# print(odd)

# t = 0
# while t > T :
#     elem_list = list(map(int,input().split()))
#     t += 1



'''
1. T의 값을 입력받는다.
2. for 를 사용해 range(T+1)만큼 반복해서 t 값을 받고, 테스트 케이스를 입력받는다.
3. 테스트 케이스를 test_list에 담는다
3. list에서 홀수만 더한 값을 구하는 함수 odd_number를 만든다
4. odd_number의 return 값은 print(f'#{t} {odd_number(test_list)}
'''


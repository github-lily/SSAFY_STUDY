import sys
sys.stdin = open('백준/test.txt')


# while True :
#     a,b,c = map(int,input().split())

#     if a == b == c == 0 :
#         break

#     if a*a + b*b == c*c :
#         print('right')
#     else :
#         print('wrong')


while True :
    lenght = sorted(map(int,input().split()))

    if sum(lenght) == 0 :
        break

    if lenght[0]**2 + lenght[1]**2 == lenght[2]**2 :
        print('right')
    else :
        print('wrong')


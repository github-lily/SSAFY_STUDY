import sys
sys.stdin = open('백준/test.txt')

def check(number) :


    N = len(number)

    for i in range(N//2) :
        if number[i] != number[-i-1] :
            print('no')
            return
            
    print('yes')
    return


while True :
    num = input()

    if num == '0' :
        break

    check(num)

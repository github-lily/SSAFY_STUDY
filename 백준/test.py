import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())

N = int(sys.stdin.readline().strip())
yes = no = 0
for _ in range(N) :
    k = int(input())    
    if k == 1 :
        yes += 1
    else :
        no += 1

if yes >= no :
    print("Junhee is cute!")
else :
    print("Junhee is not cute!")
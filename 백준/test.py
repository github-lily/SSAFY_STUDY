import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())


N = int(input())

for i in range(1,N+1) :
    spaces = ' '*(N-i)
    star = '*'*i
    print(spaces+star)
import sys
sys.stdin = open('백준/test.txt')


def find() :
    for x in range(-999,1000) :
        for y in range(-999,1000) : 
            if a*x + b*y == c and d*x + e*y ==f :
                return x,y

a,b,c,d,e,f = map(int,input().split())


x,y = find()

print(x,y)
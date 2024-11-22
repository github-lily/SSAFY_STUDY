import sys
sys.stdin = open('C:/Users/jhc03/Desktop/포트폴리오/백준/test.txt')

while True :
    a,b = map(int,input().split())
    
    # 종료조건 
    if a+b == 0 :
        break
    
    print(a+b)

    
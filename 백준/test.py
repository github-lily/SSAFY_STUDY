# import sys
# sys.stdin = open("백준/test.txt")

ans = 0
while True :
    try :
        ans += int(input())
    except EOFError :
        break
print(ans)
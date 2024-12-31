import sys
sys.stdin = open('백준/test.txt')

N = int(input())
number = list(map(int,input().split()))

ans = set()
for num in number :    
    if num == 3 or num == 5 or num == 7 :
        ans.add(num)

    elif not (num == 1 and num % 2 == 0 and num % 3 == 0  and num % 5 == 0  and num % 7 == 0)  :
            ans.add(num)

print(len(ans))
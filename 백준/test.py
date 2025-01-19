import sys
sys.stdin = open('백준/test.txt')


N,X = map(int,input().split())
lst = map(int,input().split())

num_lst = []

for num in lst :
  if num < X :
    num_lst.append(num)

print(*num_lst)
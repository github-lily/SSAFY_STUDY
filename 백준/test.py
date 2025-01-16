import sys
sys.stdin = open('백준/test.txt')


N = int(input())
arr = dict()

for _ in range(N) :
  p,l,r = input().split()
  arr[p] = [l,r]

pre_order = ''
in_order=''
post_order=''


def order(T) :
    global pre_order, in_order, post_order
    
    if T == '.' :
        return
    
    pre_order += T
    order(arr[T][0])
    in_order += T
    order(arr[T][1])
    post_order += T

order('A')

print(pre_order)
print(in_order)
print(post_order)
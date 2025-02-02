import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())

num_set = set()
for i in range(1,31) :
    num_set.add(i)


for _ in range(28) :
    n = int(input())
    num_set.remove(n)


for num in num_set :
    print(num)

import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())

num_set = set()
for _ in range(10) :
    n = int(input())

    num_set.add(n%42)

print(len(num_set))
    
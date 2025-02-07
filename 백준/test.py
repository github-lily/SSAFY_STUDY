import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())

N = int(input())

num_lst = list(map(int,input().split()))
m_val = max(num_lst)
s_val = sum(num_lst)


ans = ((s_val / m_val) * 100) / N
print(ans)
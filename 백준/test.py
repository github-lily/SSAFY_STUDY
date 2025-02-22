import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())
# import sys
# import queue

# N = int(input())
# cards = [x for x in range(1,N+1)]
# 

# while len(cards) > 1 :
#     cards.pop(0)
#     a = cards.pop(0)
#     cards.append(a)
# 
print(*cards)
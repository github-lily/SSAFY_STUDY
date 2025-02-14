import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())
import sys
import math

# 입력 받기
N = int(input())
message_set = set()
count = 0

for _ in range(N) :
    message = sys.stdin.readline().strip()
    if message == "ENTER" :
        message_set.clear()
    elif message not in message_set :
        message_set.add(message)
        count += 1

    
print(count)
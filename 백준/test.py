import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
time = 0

for char in word:
    for i in range(len(dial)):
        if char in dial[i]:
            time += i + 3

print(time)

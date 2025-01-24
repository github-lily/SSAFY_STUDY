import sys
sys.stdin = open('백준/test.txt')

T = int(input())
for _ in range(T) :
  text = list(input())
  print(text[0]+text[-1])
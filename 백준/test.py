import sys
sys.stdin = open('백준/test.txt')

N =int(input())
number = list(input())

print(sum(map(int,number)))
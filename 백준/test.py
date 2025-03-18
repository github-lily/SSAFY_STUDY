import sys
sys.stdin = open('백준/test.txt')

jongsu = input().strip()
doctor = input().strip()

if len(jongsu) >= len(doctor):
    print("go")
else:
    print("no")


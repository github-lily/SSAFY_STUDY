import sys
sys.stdin = open('백준/test.txt')

N,M = map(int,input().split())
hear = []
watch = []
union = []


for _ in range(N) :
    h = input()
    hear.append(h)

for _ in range(M) :
    w = input()
    watch.append(w)


hear = sorted(hear)
watch = sorted(watch)

for name in hear :
    if name in watch :
        union.append(name)

print(len(union))
for name in union :
    print(name)  

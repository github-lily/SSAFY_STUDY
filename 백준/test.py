import sys
sys.stdin = open('백준/test.txt')


from collections import defaultdict     # 딕셔너리 기본값 관리


N = int(input())
tang = list(map(int,input().split()))

def max_fruit_length(tang) :
    l, r = 0,0
    max_length = 0
    fruit_type = defaultdict(int)


    while r < len(tang) :
        fruit_type[tang[r]] += 1    # 현재 과일 추가

        while len(fruit_type) > 2 :
            fruit_type[tang[l]] -= 1
            if fruit_type[tang[l]] == 0 :
                del fruit_type[tang[l]]
            l += 1


        max_length = max(max_length, r-l+1)
        r += 1

    return max_length


ans = max_fruit_length(tang)
print(ans)
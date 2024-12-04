import sys
sys.stdin = open('백준/test.txt')
# 시간초과
# 아무래도 append, for문 2개,,
# N값이 100만개까지라서 초과

N = int(input())

# 원본 리스트
X = list(map(int,input().split()))

# 중복 제거 후 정렬(리스트로 반환됨)
Y = sorted(set(X))     # [-10, -9, 2, 4]

# enumerate : index, value를 반환
num_dict = {value: idx for idx, value in enumerate(Y)}      

# 결과 생성
ans = [num_dict[number] for number in X]

print(*ans)
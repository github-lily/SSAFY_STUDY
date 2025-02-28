import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())

nums = list(map(int, input().split()))  # 5개의 정수를 입력받아 리스트로 변환
verification_number = sum(n**2 for n in nums) % 10  # 각 숫자의 제곱합을 구한 뒤 10으로 나눈 나머지 계산
print(verification_number)  # 결과 출력

import sys
sys.stdin = open('백준/test.txt')

# N = int(sys.stdin.readline().strip())

S = input()  # 문자열 입력
result = [-1] * 26  # 알파벳 개수만큼 초기화

for i, char in enumerate(S):
    index = ord(char) - ord('a')  # 알파벳의 인덱스 계산
    if result[index] == -1:  # 처음 등장하는 경우만 저장
        result[index] = i

print(*result)  # 리스트를 공백으로 구분하여 출력

############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장함수 len 함수를 사용하지 않습니다.
def longest_string(str_list):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    max_string = 0 #길이가 가장 긴 문자열의 길이 저장
    ans_string = '' #정답 문자열을 저장하기 위한 변수

    for string in str_list: #리스트를 돌면서 하나의 문자열
        temp = 0 #문자열의 길이를 저장하기 위한 변수 temp
        for t in string: #리스트 내 문자열 하나를 돌면서
            temp +=1 #해당 문자열의 길이 저장
        
        if temp > max_string: #만약 해당 문자열의 길이가 max길이 값보다 크다면,
            ans_string = string #정답 문자열에 해당 문자열 할당
            max_string = temp #max값 변경

    return ans_string

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 

print(longest_string(["apple", "banana", "cherry", "date"]))  # "banana"
print(longest_string(["cat", "caterpillar", "dog", "elephant"]))  # "caterpillar"
print(longest_string(["a", "ab", "abc", "abcd"]))  # "abcd"
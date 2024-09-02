############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장함수 len 함수를 사용하지 않습니다.
def longest_string(str_list):
    
    # 여기에 코드를 작성하여 함수를 완성합니다.
    longest_keyword = str_list[0]
    for keyword in str_list :
        if len(keyword) > len(longest_keyword) :
            longest_keyword = keyword
    return longest_keyword


def longest_string(str_list):

    result = ''          #반환할 문자열(최대 길이 문자열)
    max_len = 0          #result의 길이, 지금까지 문자열 중 가장 긴 길이

    for val in str_list :
        # print(val,len(val))
        if max_len < len(val):
            max_len = len(val)
            result = val    

    return result


def longest_string(str_list):

    result = ''          #반환할 문자열(최대 길이 문자열)
    max_len = 0          #result의 길이, 지금까지 문자열 중 가장 긴 길이

    for val in str_list :
        # print(val,len(val))
        val_len = 0
        for _ in val :
            val_len += 1
        result = val

    return result

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 

print(longest_string(["apple", "banana", "cherry", "date"]))  # "banana"
print(longest_string(["cat", "caterpillar", "dog", "elephant"]))  # "caterpillar"
print(longest_string(["a", "ab", "abc", "abcd"]))  # "abcd"

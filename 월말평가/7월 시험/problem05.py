############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 set을 사용하지 않습니다.
def remove_duplicates(lst):
    new_list = []           #중복되지 않는 요소를 담을 리스트
    for elem in lst :       #리스트 요소 하나씩 빼오기
        if elem not in new_list :           #new_list 에 없으면 값 넣기
            new_list.append(elem)
    return new_list
    # 여기에 코드를 작성하여 함수를 완성합니다.

def remove_duplicates(lst):
    result = []
    for val in lst :
        if val not in result :
            result.append(val)
    
    return result

#dict로 푸는 법
def remove_duplicates(lst):
    key_dict = {}
    for key in lst :
        if key not in key_dict :
            key_dict[key] = 0
    
    return list(key_dict.keys())


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 

print(remove_duplicates([4, 5, 6, 4, 3, 2, 1, 2, 3]))  # [4, 5, 6, 3, 2, 1]
print(remove_duplicates(['a', 'b', 'c', 'a', 'd', 'b']))  # ['a', 'b', 'c', 'd']
print(remove_duplicates([4, 5, 'a', 4, 'b', 2, 'a', 3, 2, 3]))  # [4, 5, 'a', 'b', 2, 3]

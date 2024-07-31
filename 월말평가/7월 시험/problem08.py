############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 반드시 재귀 함수 형태로 구현해야 합니다.
# def reverse_string(text):

#     # 여기에 코드를 작성하여 함수를 완성합니다.
#     list_text = list(text)
#     reverse_list = list(reversed(list_text))
#     result = ''.join(reverse_list)
#     return result

def reverse_string(s):
    # 첫번째거를 뒤집음
    #'hello' -> h를 제일 마지막에 붙이고, ello를 뒤집어서 h에 붙인다
    # 그 다음에 ello에서 e를 뒤에 붙이고 llo를 붙인다

    if len(s) < 2:
        return s
    else :
        return reverse_string(s[1:]) + s


    # reverse_list = []
    # for char in text :
    #     reverse_list.append(char)




# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(reverse_string("hello"))  # "olleh"
print(reverse_string("world"))  # "dlrow"
print(reverse_string("python"))  # "nohtyp"
#####################################################

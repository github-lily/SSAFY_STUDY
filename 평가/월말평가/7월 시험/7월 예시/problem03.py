############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_user_data_valid(user_data):
    
    # 여기에 코드를 작성하여 함수를 완성합니다.

    # # Ver1
    # if user_data['id'] and user_data['password'] :
    #     return True
    # else : 
    #     return False
    
    # #Ver2
    # if user_data['id'] == '' or user_data['password'] == '' :
    #     return False
    # else : 
    #     return True

    #Ver3
    if user_data.get('id') == '' or user_data.get('password') == '' :
        return False
    return True

    #어차피 return 이후는 실행 안됨. if문이 충족되면 False에서 끝나고 충족 안되면 리턴값이 없으니 True 로 끝남
    


    #Ver4
    # if user_data.get('id') and user_data.get('password'):
    #     return True
    # return False


#에러가 안나서 실패..
    # try :
    #     return True

    # except ValueError :
    #     return False


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': '',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data1)) # False 


user_data2 = {
    'id': 'jungssafy',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data2)) # True
#####################################################
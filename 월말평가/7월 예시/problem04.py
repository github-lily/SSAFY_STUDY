############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_id_valid(user_data):
 
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # print(user_data['id'][len(user_data['id'])-1]) #값이 맞는지 확인
    try:
        int(user_data['id'][-1]) #value의 마지막자리
        return True         #int로 바꿀 수 있으면 정수란 뜻이니 True
    
    except ValueError :     #inte로 못바꾸면 False
        return False

#ValueError : 연산이나 함수에 문제가 없지만, 부적절한 값을 가진 인자를 받았고,
#상황이 IndexError 처럼 더 구체적인 예외로 설명되지 않는 경우 발생함

def is_id_valid(user_data):

   
    # 여기에 코드를 작성하여 함수를 완성합니다.
    number = '0123456789'

    
    #number = [1,2,3,4,5,6,7,8,9] 이렇게 하면 int라서 모두 False 뜰 수 있음
    
    
    value = user_data['id']
    
    if value[-1] in number:
        return True
    
    else:
        False




def is_id_valid(user_data):
    return user_data['id'][-1].isdecimal() 



def is_id_valid(user_data):
    return user_data['id'][-1].isdigit() 


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': 'jungssafy5',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data1)) # True


user_data2 = {
    'id': 'kimssafy!',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data2)) # False
#####################################################
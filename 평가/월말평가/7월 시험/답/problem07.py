############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def calculate_days_to_fill_tank(tank_capacity, fill_amount, evaporation_amount):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    day = 1 #걸리는 날짜 저장용 변수
    water = fill_amount #물탱크에 있는 물의 양 (초기값 = 낮동안 채워지는 물의 양)

    while tank_capacity > water: #물탱그의 물의 양이 총 용량 이상이면 while문 종료
        water = water - evaporation_amount + fill_amount #물탱크의 물의 양 계산
        #원래 있던 물 - 밤 동안 사라지는 양 + 낮 동안 다시 채워지는 양
        day += 1 #날짜 증가


    return day


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(calculate_days_to_fill_tank(100, 20, 5))  # 7
print(calculate_days_to_fill_tank(1000, 100, 10))  # 11
print(calculate_days_to_fill_tank(100, 10, 1))  # 11
#####################################################
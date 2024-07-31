############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def calculate_days_to_fill_tank(tank_capacity, fill_amount, evaporation_amount):
    cur_amount = 0          #현재 채워진 양
    day = 0
    while True :
        # 하루 씩 증가
        day += 1
        cur_amount =+ fill_amount
        if cur_amount >= tank_capacity:     # 다 채워지면 종류
            break
        cur_amount -= evaporation_amount
    return day


    # 여기에 코드를 작성하여 함수를 완성합니다.
    # check_water = fill_amount - evaporation_amount
    # while tank_capacity >= check_water + fill_amount :

  
    #full_tank = tank_capacity == check_water + fill_amount

    #물탱크의 총 용량 tank_capacity
    #낮시간 채워지는 물의 양 fill_amount   (day += 1)
    #밤동안 증발하는 물의 양 evaporation_amount
    #다음날 확인되는 물의 양 : fill_amount - evaporation amount = check_water
    # 전체 용량에서 빼고 더하기?



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

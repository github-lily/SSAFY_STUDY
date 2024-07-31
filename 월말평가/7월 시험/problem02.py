############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 min, max, sorted 함수 리스트 메서드 sort 를 사용하지 않습니다.

# 여기에 코드를 작성하여 함수를 완성합니다.


# max 구하기
def max_population(population_list) :
    max_people = 0
    for i in range(1,len(population_list)):
        if population_list[i] > population_list[i-1] :
            max_people = population_list[i]
    return max_people

# min 구하기
def min_population(population_list) :
    min_people = population_list[0]
    for i in range(len(population_list)) :
        if min_people > population_list[i] :
            min_people = population_list[i]
    return min_people

        

# max - min 구하기
def population_difference(population_list):
    return (max_population(population_list) - min_population(population_list))

    


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############# 테스트 코드 삭제 금지 #################
print(population_difference([100, 200, 300, 400, 500]))  # 400
print(population_difference([50, 150, 250]))  # 200
print(population_difference([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))  # 90
#####################################################

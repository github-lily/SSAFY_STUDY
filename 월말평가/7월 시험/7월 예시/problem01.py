############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 파이썬 내장 함수 min 함수를 사용하지 않습니다.

'''ver1 for문 indexing'''
def min_score(scores):
    min_s = scores[0]       #최솟값 변수 지정 #첫번째 값과 비교
    for i in range(1,len(scores)) : #첫번째 값이 기준이므로 1부터 시작
        if scores[i] <= min_s:  #최솟값과 i번째 값 비교
            min_s = scores[i]   #i번째 값이 더 작으면 최소값에 저장
    return min_s                #최종 최소값 출력

    # 여기에 코드를 작성하여 함수를 완성합니다.



'''ver2 오름차순'''
def min_score2(scores2) :
    scores2.sort()
    return scores2[0]


'''ver3 인덱싱 없는 for 문문'''
def min_score3(scores3) : 
    min_1 = scores3[0]
    for score in scores3 :
        if score < min_1 :
            min_1 = score
    return min_1
#retun 값이 나오면 함수는 끝남! 그러므로 return 이 if 문 안에 있으면 for문이 안돌고 끝나버림 주의!
    

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(min_score([30, 60, 90, 70])) # 30
print(min_score([0, 10, 20, 30, 40, 50])) # 0
print(min_score([50, 70, 50, 45, 80, 80])) # 45
#####################################################

print(min_score2([30, 60, 90, 70])) # 30
print(min_score2([0, 10, 20, 30, 40, 50])) # 0
print(min_score2([50, 70, 50, 45, 80, 80])) # 45

#####################################################

print(min_score3([30, 60, 90, 70])) # 30
print(min_score3([0, 10, 20, 30, 40, 50])) # 0
print(min_score3([50, 70, 50, 45, 80, 80])) # 45

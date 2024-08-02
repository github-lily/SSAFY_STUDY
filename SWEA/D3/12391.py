
'''
400 300 350
1000 299 578
1000 222 888
'''
'''
#찾는 쪽 번호가 mid와 같아지면 끝
1. A와 B 각각 이진 탐색을 시행한다
2. 이진 탐색을 한 바퀴 돌 때마다 cnt를 1씩 증가시킨다
3. cnt를 비교한다
'''

T = int(input())
for tc in range(1, T+1) :
    p,pa,pb = map(int,input().split())      #p : 책의 전체 쪽수/ pa, pb a와 b가 찾을 쪽 번호


    book_lst = list(range(p))          #책의 쪽수 리스트
    def find_key(lst,page,key):     #key : 찾는 page 값
        cnt = 0
        start = 1
        end = page
        while start <= end :
            mid = int((start+end)//2)
            if mid == key :
                return cnt      #검색 성공
            elif mid > key :
                end = mid
                cnt += 1
            else : #mid < key
                start = mid
                cnt += 1                    #책은 연속적으로 숫자가 있으니 값이 없는 경우는 없음!

    cnt_a = find_key(book_lst, p, pa)
    cnt_b = find_key(book_lst, p, pb)

    # print(cnt_a)
    # print(cnt_b)

    ab = int(cnt_a) - int(cnt_b)
    if ab > 0 :
        result = 'B'
    elif ab < 0 :
        result = 'A'
    else :
        result = 0
    

 


    print(f'#{tc} {result}')
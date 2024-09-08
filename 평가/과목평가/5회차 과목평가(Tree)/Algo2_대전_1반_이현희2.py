# 제출한 코드

'''
1. 문자를 ASCII 코드로 변환한다
2. 0인 최상위 비트는 제외하고, 6번부터 0번비트까지 1번에서 7번 노드에 차례로 넣는다.
3. 완전이진트리를 중외순회하여 얻은 비트열이 암호가 된다.
'''
#
# a = ord('A')
# print(a)    #65
# print(ord('A')) #65
# print(bin(ord('A')))    #0b1000001
# print(bin(3))   #0b11


# 중위순회
def inorder(v) :
    global ans, password

    if v > 7: #아래에서 0을 곱하면 오류나므로 1번부터 시작 # 노드번호로는 1번부터 7번까지
        return

    inorder(v*2)
    password.append(tree[v-1])      # 1번부터 시작했으나 실제 인덱스는 0번부터이니까 1 빼주기
    inorder(v*2+1)

    ans += ''.join(password)        # 값을 ans 에 저장한 후
    password = []                   # 다음 password 받을 수 있게 리셋


T = int(input())
for tc in range(1,T+1) :
    N = int(input())
    temp = list(input())
    bin_lst = []

    # 값을 이진수로 변환 (트리에 넣을 수 있는 형태로 변환)
    for x in temp:
        binary = bin(ord(x))
        binary = binary[2:]
        bin_lst.append(binary) #['1000001', '1000010', '1000011']

    # print(bin_lst)

    password = []
    ans = ''

    # 트리에 넣기
    tree = [0] * 7  #(0번부터 6번까지)    ['1', '0', '0', '0', '0', '0', '1']
    for k in range(len(bin_lst)) :
        for idx in range(7) :
            tree[idx] = bin_lst[k][idx]

        # 중위순회
        inorder(1)

        # print(ans)

    # # 7글자씩 끊어서 출력하기
    print(f'#{tc}', end = " ")
    last = []
    for x in range(0,len(ans),7) :
        last.append(ans[x:x+7])
    print(*last)


    #뒷칸 띄어쓰기생김
    # print(f'#{tc}', end = " ")
    # for x in range(0,len(ans),7) :
    #     print(ans[x:x+7], end = " ")
    # print()



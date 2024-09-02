import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/0902/portfolio/평가/과목평가/5회차 과목평가(Tree)/algo2_sample_in.txt")

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

'''
# 중위순회
def inorder(v) :
    global ans, password

    if v > 7: #아래에서 0을 곱하면 오류나므로 1번부터 시작 # 노드번호로는 1번부터 7번까지
        return
or x in temp:
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

    
#
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
    

'''
# 다른 풀이


def dfs(v) :
    global inorder_str
    if v > 7 : return
    dfs(v*2)
    inorder_str += bin_str[v]
    dfs(v*2+1)

T = int(input())
for tc in range(1,T+1) :
    N = int(input())
    arr = input()

    # 이진수 출력
    for ch in arr :
        val = ord(ch)
        bin_str = '0'
        for i in range(6,-1,-1) :
            if val & (1<<i) :
                bin_str += '1'
            else : 
                bin_str += '0'
        # print(bin_str)

    # 인덱스로 직접 값 지정해서 풀 수도 있음..!
    # for i in [3,1,4,0,5,2,6] :
    #     inorder_str += bin_str[i]

    inorder_str = ''


    dfs(1)
    print(inorder_str, end = ' ')
print()
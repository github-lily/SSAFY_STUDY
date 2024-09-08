import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/0902/portfolio/평가/과목평가/5회차 과목평가(Tree)/algo2_sample_in.txt")
    

#교수님 풀이

 다른 풀이


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
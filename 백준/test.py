import sys
sys.stdin = open('백준/test.txt')


L,C = map(int,input().split())
char = sorted(list(input().split()))


code = [0]*L
vowel = ['a','e','i','o','u']


def check() :
    vowel = 0
    consonant = 0

    for k in code :
        if k == 'a' or k == 'e' or k == 'i' or k == 'o' or k == 'u' :
            vowel += 1
        else :
            consonant += 1     

    if consonant >= 2 and vowel >= 1 :
        return True 

    return False



def combi(old_idx, new_idx) :
    global consonant_flag, vowel_flag

    # 암호 개수를 채우면 종료
    if new_idx == L :
        if check() :
            ans = ''.join(code)
            print(ans)
        return

    # 배열의 끝에 도달하면 종료
    if old_idx == C :
        return


    code[new_idx] = char[old_idx]
    combi(old_idx+1, new_idx+1)


    combi(old_idx+1, new_idx)
    

combi(0,0)
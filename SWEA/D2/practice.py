# 리스트에서 최소값 구하기

arr = []
def fin_min(s,e) :      #s: 시작, e: 끝
    if s == e :         #다 돌았을 때
        pass
    else :
        mid = s + e // 2
        l_mid = fin_min(s,mid)
        r_mid = fin_min(mid+1,e)

        if l_mid < r_mid :
            return l_mid
        else :
            return r_mid


result = fin_min(0,len(arr)-1)
print(arr[result])

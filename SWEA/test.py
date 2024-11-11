def btk(n,temp) : 
    if n == 4 :
        print(temp)
        return 
    
    for i in range(N) :
        if v[i] == 0 :
            btk(n,temp)
            temp.append(lst[i])
            btk(n+1, temp+[lst[i]])

N = 4
lst = [1,2,3,4]
v = [0] * N

btk(0,[])

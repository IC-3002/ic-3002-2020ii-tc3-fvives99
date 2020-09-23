def sumatoria_cubica(n):
    r=0
    for i in range(1, n+1):
        for j in range(1, i+1):
            for k in range(j,i+j+1):
                r+=1
    return r
    #raise NotImplementedError()
    #sumatoria_cubica(5)
    
def sumatoria_constante(n):
    i = (n+1)*n
    j = ((n+2)/3)
    return int(i*j)
    #raise NotImplementedError()
    #print (sumatoria_constante(5))
    

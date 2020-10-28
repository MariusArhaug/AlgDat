r = {}
def Fibo(n):    #Memoisering
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in r:
        return r[n]

    r[n] = Fibo(n-1) + Fibo(n-2)
    return r[n]

print(Fibo(40))


def fibo(n):    #bottom-up
    if n == 0 or n == 1:
        return n
    
    list = [0,1]
    for i in range(2,n+1):
        list.append(list[i-1] + list[i-2])
    return list[n]
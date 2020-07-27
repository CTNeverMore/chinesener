
def mypow(b,n):
    if b==0:
        return 0
    if n==0:
        return 1
    
    if n<0:
        b = 1/b
        n = -n
    
    result = 1
    for i in range(n):
        result *= b 
    return result 

mypow(2,-2)
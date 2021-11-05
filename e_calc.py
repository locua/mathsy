import math

#test

def fact(_n):
    """ Calculate the factorial for input integer n """
    n=1
    for i in range(1, _n+1):
        n *= i
    return n 

def calc_e(n):
    """ Calculate e """
    e=1
    for i in range(1, n):
        print(e)
        e+=(1/fact(i))
    return e

print(calc_e(100))

## Variable type plateaus as cannot handle large float???

def test_fact(n):
    out=0
    for i in range(0, n):
        if math.factorial(i) == fact(i):
            out+=1
        else:
            pass
            print(i)
            print(math.factorial(i))
    if out==n:
        print(out)
        return True
    else:
        print(out)
        return False

    
    


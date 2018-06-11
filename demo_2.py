# author_li
# create time :2018/6/10
from random import randint
import math
import time

def miller_rabin(n, k=50):
    """
    Miller-Rabin Primality Test
    Returns true if n is a (probable) prime
    Returns false if n is a composite number
    """
    if n < 6:
        return [False, False, True, True, False, True][n]
    elif n & 1 == 0:
        return False
    s = 0
    d = n - 1
    while d % 2 == 0:
        s = s + 1
        d = d >> 1
    for _ in range(k):
        a = randint(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(s-1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            elif x == n - 1:
                a = 0
                break
        if a:
            return False
    return True

if __name__ == '__main__':
    list_1=[]
    num=0
    t1=time.time()

    for i in range(2**1024,2**1025):
        if miller_rabin(i):
            num+=1
            list_1.append(i)
            if num==2:
                break
    t2=time.time()
    print(t2-t1)
    print(list_1)



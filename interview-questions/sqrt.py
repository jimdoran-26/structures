from math import *

def Solution(n):
    #return sqrt(n)

    start=0
    end=n
    m=0
    min_range = 0.00001;

    while end-start > min_range:
        m=(start+end)/2.0
        pow2=m*m

        if abs(pow2-n)<=min_range:
            return m
        elif pow2<n:
            start=m
        else:
            end=m
    return m


print(Solution(20))
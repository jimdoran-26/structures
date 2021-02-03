from math import *

def Solution(n):
    final =[]

    '''for num in range(2,n+1):
        for i in range (2,num):
            if num % i ==0:
                break
        else:
            final.append(num)'''

    for num in range(1,n+1):
        count=0
        for i in range(1,num+1):
            if num%i==0:
                count+=1
        if count==2:
            final.append(num)

    return final


print(Solution(50))
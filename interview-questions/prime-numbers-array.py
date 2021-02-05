# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.
# Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

def solution(n):
    final=[]
    for i in range(1,n+1):
        count = 0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            final.append(i)
    return final



print(solution(20))
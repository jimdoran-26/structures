#https://www.youtube.com/watch?v=kKWV8T6SAvU

#a = fist number in consecutive series, n = number of numbers in the series, N = num
#a,a+1,a+2,a+3,...a+n-1
#(a+a+n-1)*n/2= N -> (first number + last number) * n /2
#a=(2N+n-n^2)/2n

def question(N):
    final = []
    count=0
    n=2

    while 2*N+n-n**2 > 0:
        a= (2*N+n-n**2) /(2*n)

        if a==int(a):
            a=int(a)
            final.append(list(range(a,a+n,1)))
            count+=1
        n+=1
    final.insert(0,count)
    return final







print(question(100))
print(question(10))
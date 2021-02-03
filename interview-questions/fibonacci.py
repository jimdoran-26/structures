def fib(n):
    def calc(n):
        if n in [0,1]:
            return n
        else:
            return calc(n-2)+calc(n-1)
    final=[]
    for i in range(n):
        final.append(calc(i))
    return final

print(fib(7))
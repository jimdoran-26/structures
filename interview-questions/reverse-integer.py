def Solution(n):
    if n<0:
        return int('-'+str(n)[:0:-1])
    return int(str(n)[::-1])


print(Solution(20785))
print(Solution(-20785))
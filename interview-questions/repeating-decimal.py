#(1,3) -> 0.(3)
#(1,4) -> 0.25
#(1,6) -> 0.1(6)

def Solution(num,div):
    if div == 0:
        return 'undefined'
    if num ==0:
        return '0'
    if num%div ==0:
        return str(num/div)
    isNeg=False
    if num/div < 0:
        isNeg=True

    num=abs(num)
    div=abs(div)

    output = ""
    output += str(num//div)
    output += '.'

    num_q=[]

    while True:
        rem = num%div
        if rem==0:
            for i in num_q:
                output+=str(i[-1])
            break


        num=10*rem
        q=num//div

        if [num,q] not in num_q:
            num_q.append([num,q])


        elif [num,q] in num_q:
            ind = num_q.index([num,q])
            for i in num_q[:ind]:
                output+=str(i[-1])

            output+= '('
            for i in num_q[ind:]:
                output+=str(i[-1])
            output+=')'
            break

    return (output)











print(Solution(10,3))
print(Solution(1,4))
print(Solution(1,6))
print(Solution(0,4))
print(Solution(4,0))
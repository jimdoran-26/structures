def Solution(s):
    temp ={}
    for i in s:
        if i in temp:
            temp[i]+=1
        else:
            temp[i]=1

    for i in range(len(s)):
        if temp[s[i]]==1:
            return i
    return -1



print(Solution('alphabet'))
print(Solution('barbados'))
print(Solution('crunchy'))
print(Solution('aaaaaa'))
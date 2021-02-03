def Solution(lst,target):
    #O(n^2)
    '''for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==target:
                return [i,j]'''

    complementMap = {}

    for i in range(len(lst)):
        num = lst[i]
        complement = target-num

        if num in complementMap:
            return [complementMap[num],i]
        else:
            complementMap[complement]=i


print(Solution([2,7,11,19],9))
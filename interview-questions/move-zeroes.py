#Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of
#the non-zero elements.
def solution(arr):
    for i in arr:
        if 0 in arr:
            arr.remove(0)
            arr.append(0)
    return arr





array1 = [0,1,0,3,12]
array2 = [1,7,0,0,8,0,10,12,0,4]


print(solution(array1))
print(solution(array2))

# Given an array containing None values fill in the None values with most recent
# non None value in the array
def solution(arr):
    for i in range(len(arr)):
        if arr[i]==None:
            arr[i]=arr[i-1]
    return arr






array1 = [1,None,2,3,None,None,5,None]
print(solution(array1))
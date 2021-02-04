# Given an array of integers, determine whether the array is monotonic or not.
def solution(arr):
    inc=0
    dec=0
    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            inc=1
        elif arr[i] > arr[i+1]:
            dec=1
    return dec ^ inc


A = [6, 5, 4, 4]
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]
print(solution(A))
print(solution(B))
print(solution(C))
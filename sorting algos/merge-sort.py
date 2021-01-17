def merge(left, right):
    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:#compare left to right
            result.append(left[left_index])#if left is less than right
            left_index += 1
        else:
            result.append(right[right_index])#if right is less than left
            right_index += 1

    result += left[left_index:]#rest of left
    result += right[right_index:]#rest of right
    return result


def merge_sort(array):
    if len(array) <= 1:  # base case single element
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)

array = [4, 2, 3, 8, 8, 43, 6,1, 0]
ar = merge_sort(array)
print(ar)

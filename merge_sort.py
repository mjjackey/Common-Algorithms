def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


def merge_sort(arr):
    import math
    if(len(arr)<2):
        return arr
    middle = math.floor(len(arr)/2)
    left,right=arr[0:middle],arr[middle:]
    return merge(merge_sort(left),merge_sort(right))


if __name__ == "__main__":
    arr = [6, 1, 7, 9, 2, 4, 3, 5, 10, 8]
    result_arr=merge_sort(arr)
    print(result_arr)
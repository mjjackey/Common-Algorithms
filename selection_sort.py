def selection_sort(arr):
    n=len(arr)
    if n<2:
        print("The array's length is less than 2!")
    for i in range(n):
        max_index=i
        for j in range(i+1,n):
            if arr[i]<arr[j]:
                max_index=j
        arr[i],arr[max_index]=arr[max_index],arr[i]
    return arr

if __name__=="__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("The array before sort: ", arr)
    print("The array after sort:", selection_sort(arr))
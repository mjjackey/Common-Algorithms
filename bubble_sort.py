def bubble_sort(arr):
    n=len(arr)
    if n<2:
        print("The array length is less than 2!")
    else:
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j]<arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

if __name__=="__main__":
    arr=[64, 34, 25, 12, 22, 11, 90]
    print("The array before sort: ", arr)
    print("The array after sort:", bubble_sort(arr))

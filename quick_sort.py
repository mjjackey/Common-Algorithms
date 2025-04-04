def quick_sort(data, low, high):
    if low<high:
        pivotkey=data[low]
        i=low
        j=high
        while i<j:
            while i<j and data[j]>=pivotkey:
                # find the data which is smaller than pivotkey,from the array's high index
                j-=1
            if i<j:
                data[i]=data[j] # move the data to the low index
                i+=1
            while i<j and data[i]<=pivotkey:
                # find the data which is bigger than pivotkey,from the array's low index
                i+=1
            if i<j:
                data[j]=data[i] # move the data to the high index
                j-=1
        data[i]=pivotkey
        quick_sort(data,low,i-1)
        quick_sort(data,i+1,high)

if __name__ == "__main__":
    data=[6,1,7,9,2,4,3,5,10,8]
    low=0
    high=9
    quick_sort(data,low,high)
    print(data)
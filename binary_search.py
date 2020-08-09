def binarySearch(L,e,low,high):
    """
    Binary Search
    :param L: The sorted list
    :param e: The number to look for
    :param low: The lowest index
    :param high: The highest index
    :return: bool: whether to find the number
    """
    if(L==[]): return False

    if high == low:
        return L[low] == e
    elif low>high:
        return False

    mid = int((low+high)/2)
    if L[mid]==e:
        return True
    elif L[mid]>e:
        # if low == mid: # equals to above statement "elif low>high"
        #     return False
        return binarySearch(L,e,low, mid-1)
    else:
        # if high == mid: # equals to above statement "elif low>high"
        #     return False
        return binarySearch(L,e,mid+1,high)

def binarySearch2(L,e,low,high):
    """
    Binary Search
    :param L: The sorted list
    :param e: The number to look for
    :param low: The lowest index
    :param high: The highest index
    :return: bool: whether to find the number
    """
    if(L==[]): return False
    while(low<=high):
        mid=(low+high)//2
        if(L[mid]==e): return mid
        elif(e<L[mid]):  high=mid-1
        else: low=mid+1

    return False

def search(L,e):
    result = binarySearch(L,e,0,len(L)-1)
    print(result)
    result2 = binarySearch2(L, e, 0, len(L) - 1)
    print(result2)


if __name__=="__main__":
    L = range(10);
    e = 8
    search(L, e)

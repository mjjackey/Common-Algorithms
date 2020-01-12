def binarySearch(L,e,low,high):
    """
    Binary Search
    :param L: The sorted list
    :param e: The number to look for
    :param low: The lowest index
    :param high: The highest index
    :return: bool: whether to find the number
    """
    if high == low:
        return L[low] == e
    mid = (low+high)//2
    if L[mid]==e:
        return True
    elif L[mid]>e:
        if low == mid:
            return False
        else:
            return binarySearch(L,e,low, mid-1)
    else:
        if high == mid:
            return False
        return binarySearch(L,e,mid+1,high)

def search(L,e):
    result = binarySearch(L,e,0,len(L)-1)
    print(result)

L = range(10);
e = 8

search(L,e)

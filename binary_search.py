def binarySearch(L,e,low,high):
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
        return binarySearch(L,e,mid+1,high)

def search(L,e):
    result = binarySearch(L,e,0,len(L)-1)
    print(result)

L = range(10);
e = 7

search(L,e)

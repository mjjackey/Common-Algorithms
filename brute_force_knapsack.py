"""
Brute Force Algorithm
items, A B C D E F G
weithts, 35kg 30kg 6kg 50kg 40kg 10kg 25kg
values, 10 40 30 50 35 40 30
The code is from https://blog.csdn.net/changyuanchn/article/details/51417796
each bit represents each status of items(take:1 or not take:0), the bits number is 7
the option number is C7_0+C7_1+...C7_7 i.e. 2^7
"""
import time

# item have three attributes: name,weight,value
class Item(object):
    def __init__(self,n,v,w):
        self.name=n
        self.weight=float(w)
        self.value=float(v)

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        result = ' < '+self.name+' , '+str(self.value)+' , '+str(self.weight) + '>'
        return result

def buildItem():
    names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    weights = [35, 30, 6, 50, 40, 10, 25]
    vals = [10, 40, 30, 50, 35, 40, 30]
    Items = []  # a list of Item class
    for i in range(len(names)):
        Items.append(Item(names[i], vals[i], weights[i]))
    return Items

def getBinaryRep(n,numDigitals):
    """
    Get the binary representation of value n,
    numDigitals is the number of bits
    """
    result=''
    while n>0:
        result=str(n%2)+result
        n=n//2

    if len(result)> numDigitals:
        raise ValueError("not enough digits")

    for i in range(numDigitals - len(result)):  # add 0 according to numDigitals
        result = '0'+result

    return result

def genPowerSet(L):
    """
    Get all possible options of components of L
    :param L: a list of item class
    :return: a list of picked items list
    """
    powerset=[]
    for i in range(2**len(L)): # for each value representing each option
        binstr = getBinaryRep(i,len(L))
        subset = []

        for j in range(len(L)): # check each bit(status), j is subscript
            if binstr[j]=='1':
               subset.append(L[j])  #subset includes all items which is 1 means contained in a knapsack
        powerset.append(subset)
    return powerset

# Brute-force method
def chooseBest(pset, maxWeight, getVal, getWeight):
    """
    :param pset: a list of picked items list
    :param maxWeight:
    :param getVal:
    :param getWeight:
    :return: (items set, max value)
    """
    bestVal = 0.0
    bestSet = None
    for items in pset:  # items is a list whose element is each option(item) of components
        itemsVal = 0.0
        itemsWeight = 0.0
        for i in range(len(items)):
            itemsVal += getVal(items[i])
            itemsWeight += getWeight(items[i])
            if i== len(items)-1 and itemsWeight <= maxWeight and itemsVal > bestVal:
                bestVal = itemsVal
                bestSet = items
    return (bestSet, bestVal)


def testBest(maxWeight=150):
    items = buildItem()
    pset = genPowerSet(items)
    taken, val = chooseBest(pset, maxWeight, Item.getValue, Item.getWeight)
    print('Total value of items taken = ', val)
    for item in taken:
        print(item)

if __name__ == "__main__":
    start1 = time.time()
    testBest()
    end1 = time.time()
    print("runing time is %f" % (end1 - start1))





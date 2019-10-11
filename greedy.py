"""
Greedy Algorithm
The code is from https://blog.csdn.net/changyuanchn/article/details/51417796
"""
import brute_force as bf

def value(item):
    return item.getValue()

def weightInverse(item):
    return 1.0/item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()

def greedy(items,maxWeight,keyFunction):
    itemsCopy = sorted(items,key=keyFunction,reverse = True)  ####
    result = []
    totalValue = 0.0
    totalWeight = 0.0
    for i in range(len(itemsCopy)):
        if(totalWeight + itemsCopy[i].getWeight()) <= maxWeight:
            result.append(itemsCopy[i])
            totalValue +=itemsCopy[i].getValue()
            totalWeight +=itemsCopy[i].getWeight()
    return (result,totalValue)

def testGreedy(items,constraint,keyFunction):
    taken,val=greedy(items,constraint,keyFunction)
    print('Total value of items taken = ', val)
    for item in taken:
        print(' ', item)

def testGreedys(maxWeight = 150):
    items = bf.buildItem()

    print('Use greedy by value to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, value)

    print('\n Use greedy by weight to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, weightInverse)

    print('\n Use greedy by density to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, density)

if __name__ == "__main__":
        testGreedys()

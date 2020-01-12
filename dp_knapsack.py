
import  brute_force_knapsack as bf
def maxValue(oraSet,leftRoom):
    """
    Binary tree recursion
    Refer to https://blog.csdn.net/changyuanchn/article/details/51429979
    :param oraSet: the list of items which have not been picked
    :param leftRoom: the ramaining weight of knapsack
    :return:(value, a tuple of items which have been picked)
    """
    # leaf
    if oraSet == [] or leftRoom == 0:
        return (0,())
    # only right tree
    elif oraSet[0].getWeight() > leftRoom:
        result = maxValue(oraSet[1:],leftRoom)
    # select the best from the left and right
    else:
        # left tree, means we select nextItem(the first value of the remaining)
        nextItem = oraSet[0]
        leftVal, leftTaken = maxValue(oraSet[1:], leftRoom - nextItem.getWeight())
        leftVal +=nextItem.getValue()

        # right tree,means we do not select nextItem
        rightVal,rightTaken = maxValue(oraSet[1:],leftRoom)

        if leftVal > rightVal:
            result = (leftVal,leftTaken+(nextItem,))
        else:
            result = (rightVal,rightTaken)

    return result


def fastMaxVal(oraSet, leftWeight, memo={}):
    """
    Dynamic Programming for Binary tree recursion
    Refer to https://blog.csdn.net/changyuanchn/article/details/51429979
    :param oraSet: the list of items which have not been picked
    :param leftWeight: the ramaining weight of knapsack
    :param memo: store the existing return which is in a dictionary,(len(oraSet),leftWeight) is key
    :return:(value, a tuple of items which have been picked)
    """
    if (len(oraSet), leftWeight) in memo:
        result = memo[(len(oraSet), leftWeight)]
    elif oraSet == [] or leftWeight == 0:
        result = (0,())
    elif oraSet[0].getWeight()>leftWeight:
        result = fastMaxVal(oraSet[1:], leftWeight, memo)
    else:
        nextItem = oraSet[0]

        leftValue,leftToken = fastMaxVal(oraSet[1:], leftWeight - nextItem.getWeight(), memo)
        leftValue +=nextItem.getValue()

        rightValue,rightToken = fastMaxVal(oraSet[1:], leftWeight, memo)

        if leftValue >rightValue:
            result = (leftValue,leftToken+(nextItem,))
        else:
            result = (rightValue,rightToken)

    memo[(len(oraSet), leftWeight)] = result

    return result


def testCode():
    value,taken = maxValue(bf.buildItem(), 150)
    for item in taken:
        print(item)
    print("Total value of tokens is ", value)

def testCode2():
    value, taken = fastMaxVal(bf.buildItem(), 150)
    for item in taken:
        print(item)
    print("Total value of tokens is ", value)

if __name__ == "__main__":
    testCode()
    testCode2()
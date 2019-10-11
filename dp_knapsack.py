
import  brute_force as bf
def maxValue(oraSet,leftRoom):
    """
    Binary tree recursion
    Reference to https://blog.csdn.net/changyuanchn/article/details/51429979
    :param oraSet: the items list have not been picked
    :param leftRoom: the ramaining weight of knapsack
    :return:(value, items have been picked)
    """
    # leaf
    if oraSet == [] or leftRoom == 0:
        return (0,())
    # only right tree
    elif oraSet[0].getWeight() > leftRoom:
        result = maxValue(oraSet[1:],leftRoom)
    # select the best from the left and right
    else:
        # left tree, means we select nextItem(the first value of the remains)
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


def fastMaxVal(oraSet,leftRoom,memo={}):
    """
    Dynamic Programming for Binary tree recursion
    Reference to https://blog.csdn.net/changyuanchn/article/details/51429979
    :param oraSet: the items list have not been picked
    :param leftRoom: the ramaining weight of knapsack
    :param memo: store the existing return which is a dictionary,(len(oraSet),leftRoom) is key
    :return:(value, items have been picked)
    """
    if (len(oraSet),leftRoom) in memo:
        result = memo[(len(oraSet),leftRoom)]
    elif oraSet == [] or leftRoom == 0:
        result = (0,())
    elif oraSet[0].getWeight()>leftRoom:
        result = fastMaxVal(oraSet[1:],leftRoom,memo)
    else:
        nextItem = oraSet[0]

        leftValue,leftToken = fastMaxVal(oraSet[1:],leftRoom - nextItem.getWeight(),memo)
        leftValue +=nextItem.getValue()

        rightValue,rightToken = fastMaxVal(oraSet[1:],leftRoom,memo)

        if leftValue >rightValue:
            result = (leftValue,leftToken+(nextItem,))
        else:
            result = (rightValue,rightToken)

    memo[(len(oraSet),leftRoom)] = result

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
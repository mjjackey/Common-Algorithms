import math
def generate_prime():
    n=100
    pri_num_list=[]
    for num in range(2, n + 1):
        if all(num % j != 0 for j in range(2, int(math.sqrt(num))+1)):
            pri_num_list.append(num)
    print(len(pri_num_list),pri_num_list)

def generate_prime2():
    n = 100
    pri_num_list = []
    for num in range(2,n+1):
        flag = True
        for j in range(2, int(math.sqrt(num)+1)):
            if(num%j==0):
                flag=False
                break
        if(flag):
            pri_num_list.append(num)
    print(len(pri_num_list), pri_num_list)

def generate_prime3():
    n = 100
    pri_num_list = []
    for num in range(2, n + 1):
        flag = True
        for j in range(2, int(math.sqrt(num) + 1)):
            for k in range(2, int(math.sqrt(j) + 1)):
                if (j % k == 0):
                    flag = False
                break
        if (flag):
            pri_num_list.append(num)
    print(len(pri_num_list), pri_num_list)

generate_prime2()
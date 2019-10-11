def fastFib(n,memo={}):
    if n==0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1,memo) + fastFib(n-2,memo)
        memo[n] = result
        return result

past_fib={}
def fast_fib2(n):
    if n in past_fib:
        return past_fib[n]
    if n == 0 or n == 1:
        past_fib[n] = 1
        return 1
    total = fast_fib2(n - 1) + fast_fib2(n - 2)
    past_fib[n] = total
    return total

import time
if __name__ == "__main__":
    n = 120
    start = time.time()
    result=fastFib(n)
    end = time.time()
    print(result)
    print("Fibnacci sequense costs", end - start)

    start1 = time.time()
    result1 = fast_fib2(n)
    end1 = time.time()
    print(result1)
    print("Fibnacci sequense costs", end1 - start1)



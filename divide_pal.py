def isPal(s):
    if len(s) <= 1:
        return True
    else:
        return s[0]==s[-1] and isPal(s[1:-1])  #s[1:-1] omit the first and the last element

if __name__ == "__main__":
    s = 'doggod'
    result = isPal(s)
    print(result)

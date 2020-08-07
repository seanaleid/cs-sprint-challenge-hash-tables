def has_negatives(a):
    # initialize result
    result = []
    # initialize dict with list a
    # 1. Put whole list in a dict
        # needed .fromkeys()
        # will zip work? --> about the same speed
    d = dict.fromkeys(a)
    # d = dict(zip(a, a))
    # print(d)
    # 2. Loop over the list
    for num in a:
        # 2.1 Check if num is positive and if negative num in dict
        if num > 0 and -num in d:
            # 2.2 If yes, append to list 
            result.append(num)
    # 3. Return list
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

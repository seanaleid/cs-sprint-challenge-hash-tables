def intersection(arrays):
    # initialize result list
    result = []
    # initialize dict
    d = dict()

    # 1. Loop over array in arrays
    for array in arrays:
        # Loop over num in array
        for num in array:
            # Check if num is in the dict
            if num in d:
                # check if in the result array
                if num in result:
                    pass
                # Yes, append to result list
                else:
                    result.append(num)
            else:
                # No, add to dict
                d[num] = num
    
    # 2. Return result list
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

def get_indices_of_item_weights(weights, length, limit):
    # initialize dict
    d = dict()

    # 1. Put weights into dict, using weight value as key and list index as value
    for i in range(len(weights)):
        # need () around weights[i] for the array of [4,4], dicts don't like duplicates
        d[(weights[i])] = i
    
    # 2. Check for edge cases
    if length < 2:
        return None
    elif length ==2 and weights[0] == weights[1]:
        return (1,0)
    
    # 3. Loop over weights and subtract limit
    else:
        for weight in weights:
            # check if in dict
            if limit - weight in d:
                # create tuple
                weight_index_var = (d[weight], d[limit-weight])
                t = (max(weight_index_var), min(weight_index_var))
                # return tuple
                return t

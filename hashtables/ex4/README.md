# Positive and Negative

For an input list of integers, we wish to know which positive numbers
have corresponding negative numbers in the list.

Example input:

```python
[ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]
```

Input can be in any order.

Example return value:

```python
[ 1, 3, 4 ]
```

Because 1, 3, and 4 are the positive numbers that have corresponding
negative numbers in the list.

Return value can be in any order.

Solve this problem with a hash table.

Limits:

* The input list can contain approximately 5,000,000 elements.

* U --> Find the positive numbers that have negative numbers in the list. Order doesn't matter.
* P --> 
    # 1. Put whole list in a dict
    # 2. Loop over the list
        # 2.1 Check if num is positive and if negative num in dict
        # 2.2 If yes, append to list 
    # 3. Return list
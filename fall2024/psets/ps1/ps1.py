from asyncio import base_tasks
import math
import time
import random

"""
See below for mergeSort and singletonBucketSort functions, and for the BC helper function.
"""


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def singletonBucketSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        raise ValueError()
    return digits

def radixSort(univsize, base, arr):
    """TODO: Implement Radix Sort using BC and singletonBucketSort"""
    k = int(math.log(univsize, base)) + 1

    BCarr = []
    for i in range(len(arr)):
        BCarr.append((BC(arr[i][0], base, k), arr[i][1]))

    for j in range(k):
        forSort = []
        for i in range(len(BCarr)):
            forSort.append((BCarr[i][0][j], BCarr[i][0], BCarr[i][1]))
        sortedArr = singletonBucketSort(base, forSort)
        BCarr = [(item[1], item[2]) for item in sortedArr]
    
    result = []
    for i in range(len(BCarr)):          
        temp = 0
        digits = BCarr[i][0]
        for place_value in range(k):
            temp += digits[place_value] * (base ** place_value)
        result.append((temp, BCarr[i][1]))

    return result
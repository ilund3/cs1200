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
    """Implement Radix Sort using BC and singletonBucketSort"""
    k = int(math.log(univsize, base)) + 1  # Number of digits

    # Convert numbers to their base-b digit representation
    for i in range(len(arr)):
        arr[i] = (BC(arr[i][0], base, k), arr[i][1])  # arr[i] = (digits_list, value)

    # Perform sorting for each digit position
    for j in range(k):
        forSort = []
        for i in range(len(arr)):
            digits_list, value = arr[i]
            digit = digits_list[j]
            # Build tuples with the current digit for sorting
            forSort.append((digit, digits_list, value))
        # Sort based on the current digit
        forSort = singletonBucketSort(base, forSort)
        # Update arr with the sorted tuples, maintaining the consistent structure
        arr = []
        for elt in forSort:
            # elt is (digit, digits_list, value)
            arr.append((elt[1], elt[2]))  # arr[i] = (digits_list, value)

    # Reconstruct the original numbers from the digits_list
    for i in range(len(arr)):
        digits_list, value = arr[i]
        temp = 0
        for place_value in range(k):
            temp += digits_list[place_value] * (base ** place_value)
        arr[i] = (temp, value)
    return arr

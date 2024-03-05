import math
import os
import random
import re
import sys


def maxMin(k, arr):
    # Write your code here
    arr.sort()  

    min_unfair = float('infinity') 

    for i in range(len(arr) - k + 1):
        unfairness = arr[i + k - 1] - arr[i]  
        min_unfair = min(min_unfair, unfairness) 
    return min_unfair

if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

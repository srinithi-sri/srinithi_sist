import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    # Write your code here
    sum=0
    for i in range(len(arr)):
        sum=sum+arr[i]
    print ( sum-max(arr), sum-min(arr))

if _name_ == '_main_':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

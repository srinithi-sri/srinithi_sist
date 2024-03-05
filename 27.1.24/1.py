import math
import os
import random
import re
import sys

def anagram(s):
    # Write your code here
    if len(s) % 2 == 1:
        return -1
    s1 = s[:int(len(s) / 2)]
    s2 = s[int(len(s) / 2):]
    a = list(set(s2))
    count = 0
    for c in a:
        count += max(s2.count(c) - s1.count(c), 0)
    return count

if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()

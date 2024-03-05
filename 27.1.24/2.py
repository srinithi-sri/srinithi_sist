import math
import os
import random
import re
import sys

def timeConversion(s):
    time_12h = datetime.strptime(s, "%I:%M:%S%p")
    time_24h = time_12h.strftime("%H:%M:%S")

    return time_24h


if _name== '__main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

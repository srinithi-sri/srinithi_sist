import math
import os
import random
import re
import sys



if _name_ == '_main_':
    n = int(input().strip())
    if(n%2 != 0):
        print("Weird")
    elif (n%2==0 and n in range(2,5)):
        print("Not Weird")
    elif (n%2==0 and n in range(6,20)):
        print("Weird")
    else:
        print("Not Weird")

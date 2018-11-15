#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    max_arr = Counter(ar) # produces a dictionary
    no_of_times_max = max(max_arr.values()) # Find the max value of the dictionary
    return(no_of_times_max)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

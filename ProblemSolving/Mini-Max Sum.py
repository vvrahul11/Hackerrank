#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum_no = reduce(lambda x, y : x + y, arr)
    min_number = sum_no - max(arr)
    max_number = sum_no - min(arr)
    print(min_number, max_number)
        

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


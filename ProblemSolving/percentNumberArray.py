#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p_f=  len(list(filter(lambda x : x > 0, arr)))/len(arr)
    n_f = len(list(filter(lambda x : x < 0, arr)))/len(arr)
    z_f = len(list(filter(lambda x : x == 0, arr)))/len(arr)
    print("%.6f" % p_f)
    print("%.6f" % n_f)
    print("%.6f" % z_f)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


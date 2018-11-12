#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    myArray = list(i+1 for i in range(n))
    myreversedArray = list(reversed(list(j for j in range(n))))

    print(myArray)
    print(myreversedArray)
    
    myShapes = list(map(lambda x : x * '#', myArray))
    myGaps =   list(map(lambda y : y * ' ', myreversedArray))

    k = list(map(lambda x, y : print(y + x), myShapes, myGaps))

if __name__ == '__main__':
    n = int(input())

    staircase(n)


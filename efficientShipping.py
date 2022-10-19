#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMaxUnits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY boxes
#  2. LONG_INTEGER_ARRAY unitsPerBox
#  3. LONG_INTEGER truckSize
#

def getMaxUnits(boxes: list[int], unitsPerBox: list[int], truckSize: int) -> int:
    # create a 2D array for boxes and units
    data: list[tuple[int, int]] = list(zip(boxes, unitsPerBox))

    # sort by the number of units per box
    data.sort(key=lambda el: el[1], reverse=True)

    res, remainingSpace = 0, truckSize

    for boxCount, unitCount in data:
        # can't have more boxes than truck's max capacity
        realBoxCount: int = min(truckSize, boxCount)

        # box times the units in the box
        res += realBoxCount * unitCount

        # reduce the remaining space
        remainingSpace -= realBoxCount

        if remainingSpace <= 0:
            break

    return res

print(getMaxUnits([1,3,2], [3,1,2], 3))

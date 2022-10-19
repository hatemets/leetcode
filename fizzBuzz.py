#!/bin/python3

import math
import os
import random
import re
import sys

def minimalOperations(words: list[str]) -> list[int]:
    res: list[int] = []

    for word in words:
        wordLen: int = len(word)
        count: int = 0
        i: int = 0
        isChecked: bool = False

        # compare the letters in pairs
        while i < wordLen:
            # if the character hasn't been checked (from the previous iteration), then consider it for checking
            if not isChecked and i < wordLen - 1 and word[i] == word[i + 1]:
                count += 1
                isChecked = True
            elif isChecked:
                isChecked = False
            i += 1

        res.append(count)

    return res

print(minimalOperations(["add", "boook", "break", "aaabb"]))
# print(minimalOperations(["aaabb"]))

import math
import os
import random
import re
import sys


def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])
        
    tmpArr = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
    answer = ""
    for i in range(len(tmpArr)):
        tmp = sorted(tmpArr[i])
        if tmp != tmpArr[i]:
            answer = "NO"
            break
    return "YES" if answer == "" else "NO"
    


print(gridChallenge(['kc', 'iu']))


import math
import os
import random
import re
import sys


def getMinimumCost(k, c):
    answer = 0
    c.sort(reverse = True)

    flowerNum = 0
    for cost in c:
        currentCost = (flowerNum//(k)+1) * (cost)
        flowerNum += 1
        answer += currentCost

    return answer


print(getMinimumCost(3, [2, 5, 6]))
import math
import os
import random
import re
import sys


def maxMin(k, arr):
    arr.sort()
    answer = 10**9

    for i in range(0, len(arr)-k+1):
        tmp = arr[i:i+k]
        answer = min(tmp[-1]-tmp[0], answer)
    return answer

print(maxMin(3, [10, 100, 300, 200, 1000, 20, 30]))
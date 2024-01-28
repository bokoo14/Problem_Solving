import math
import os
import random
import re
import sys

def minimumAbsoluteDifference(arr):
    answer = 10**9
    arr = sorted(arr)
    for i in range(0, len(arr)):
        answer = min(abs(arr[i]-arr[i-1]), answer)
    answer = min(abs(arr[0]-arr[-1]), answer)
    return answer


print(minimumAbsoluteDifference([1, -3, 71, 68, 17]))
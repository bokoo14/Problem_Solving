import math
import os
import random
import re
import sys


def equal(arr):
    min_value=min(arr)
    min_operations=math.inf

    for i in range(5):
        now_min_operations=0
        for x in arr:
            t=x-min_value
            now_min_operations+=t//5 # 5를 더하는 횟수
            t=t% 5
            now_min_operations+=t//2 # 2를 더하는 횟수
            now_min_operations+=t% 2 # 1을 더하는 횟수
        min_operations = min(min_operations, now_min_operations)
        min_value-=1
    return min_operations
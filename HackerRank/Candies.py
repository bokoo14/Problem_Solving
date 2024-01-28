import math
import os
import random
import re
import sys

def candies(n, arr):
    candyNum = [1]*n
    
    for i in range(n-1):
        if arr[i] < arr[i+1] and candyNum[i] >= candyNum[i+1]:
            candyNum[i+1] = candyNum[i]+1
        elif arr[i] > arr[i+1] and candyNum[i] <= candyNum[i+1]:
            candyNum[i] = candyNum[i+1]+1

    for i in range(n-1, 0, -1):
        if arr[i] < arr[i-1] and candyNum[i] >= candyNum[i-1]:
            candyNum[i-1] = candyNum[i]+1
        elif arr[i] > arr[i-1] and candyNum[i] <= candyNum[i-1]:
            candyNum[i] = candyNum[i-1]+1

    return sum(candyNum)

print(candies(10, [2,4,2,6,1,7,8,9,2,1]))
print(candies(8, [2,4,3,5,2,6,4,5]))
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    cost_dict = {}
    for i,icost in enumerate(cost):
        #money: 4
        #input : 1 4 5 3 2
        #0,1
        #1,4
        #2,5
        #3,3
        #4,2

        #2 2 4 3
        #0,2
        #1,2
        #2,4
        #3,3 
        if money-icost in cost_dict:
            print(str(cost_dict[money-icost]+1) + ' ' + str(i+1))
            return 
        else:
            cost_dict[icost] = i
            
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)

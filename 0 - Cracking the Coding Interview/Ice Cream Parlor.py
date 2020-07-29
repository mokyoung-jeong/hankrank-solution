#!/bin/python3

import math
import os
import random
import re
import sys

"""
문제: 주어진 돈으로 ,두개의 아이스크림을 살수있도록  아이스크림 index를 찾아라. 
      조건: 주어진 아이스크림 리스트에는 한쌍의 결과만 존재한다. 
      
문제 전급법: 
- 아이스크림인덱스별 가격들중 두개의 합이 money 값과 같다. 
=> ( 2<= N  <=10의 4승 ) 
=> ( 1<=cost[n] <=  5*10 9승) 
=> money =cost[n] +cost[!n]     ->  money - cost[n] = cost[!n] 
=> cost[!n]=> cost_dictionary:  아이스크림 값 키로한 hash map 으로 만든다. 

money: 4
input : 1 4 5 3 2
0,1
1,4
2,5
3,3
4,2

        #2 2 4 3
        #0,2
        #1,2
        #2,4
        #3,3 

"""
# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    cost_dict = {}
    for i,icost in enumerate(cost):
  
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

#!/bin/python3

import math
import os
import random
import re
import sys


"""
magazin 를 받아. magazin dictionry 만들기 

"""
# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
     answer = 'Yes'
     magazine_dic = {}

    
     for i in range(len(magazine)):
         if magazine[i] not in magazine_dic.keys():
             magazine_dic[magazine[i]] = 1
         else:
             magazine_dic[magazine[i]] = magazine_dic[magazine[i]] + 1
 
     for i in range(len(note)):
         if note[i] not in magazine_dic.keys():
             answer = 'No'
             break
         else:
             magazine_dic[note[i]] = magazine_dic[note[i]] - 1
             if magazine_dic[note[i]] < 0:
                 answer = "No"
                 break   
     
     print(answer)


    

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

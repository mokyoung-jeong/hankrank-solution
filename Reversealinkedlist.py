#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)
            
# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
"""
문제 :  주어진 N개의 입력값을 입력의 역링크드리스트들로 만들어라. 

input 첫라인: 테스트 리스트 갯수 T  
input 두번째: 각 테스트리스트의 엘리먼트 갯수 N  
input 세번째: 각 엘리먼트 값 element[1..N]
총입력 : list[1...T]
example_input :
3  # 리스트 3개가 주어진다. 
4  # 1 번째 리스트는 엘리먼트가 4개다 .
1  # 1 번째 리스트의 1번째 엘리먼트
2  # 1 번째 리스트의 ...
3  # 1 번째 리스트의 ...
4  # 1 번째 리스트의 ...4번째 
5  # 2 번째 리스트의 엘리먼트가 5개다 .
9  # 2 번째 리스트의 1번째 엘리먼트.
7  # 2 번째 리스트의
8  # 2 번째 리스트의
5  # 2 번째 리스트의
1  # 2 번째 리스트의 5번째 엘리먼트  
6  # 3 번째 리스트의 엘리먼트 갯수는 6개이다. 
10 # 3 번째 리스트의 1번째 엘리먼트
8  # 3 번째 리스트의
11 # 3 번째 리스트의
3  # 3 번째 리스트의
8  # 3 번째 리스트의
5  # 3 번째 리스트의 6번째 엘리먼트 



output:
4 3 2 1
1 5 8 7 9
5 8 3 11 8 10
"""
def reverse(head):
    if head is None:
      return head
    
    last = None
    current = head
    while(current is not None):
        next_node = current.next
        current.next = last 
        last = current
        current = next_node

    return last

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node
 

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

"""
문제 :  
- 양방향 링크드 리스트로 주어진다. 
- 주어진 N개의 입력값을 입력의 역링크드리스트들로 만들어라. 
input 첫라인: 테스트 리스트 갯수 T, 총 리스트갯수   
input 두번째: 각 테스트리스트의 엘리먼트 갯수 N  
input 세번째: 각 엘리먼트 값 element[1..N]
총입력 : list[1...T]
해결방법 : 
- last, current, nextnode pointer 를 사용 
- last는 가장 최근 이전의 노드를 가르킨다. (첫 값은  none)
- nextnode는 다음 앞의 노드를 가리킨다. 
- current는 노드를 한단계씩이동하여, current.next point 를 last 로 역으로 연결하여 역순 링크드 리스트를 만든다. 

explane_input :
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
explain_output:
4 3 2 1
1 5 8 7 9
5 8 3 11 8 10


sample input:
1
5
1
2
3
4
5
sample_output: 
5 4 3 2 1
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

def reverse(head):
    if head == None:
        return
    
    current = head
    prev = None
    
    while current != None:
        nxt = current.next
        current.prev = nxt
        current.next = prev
        prev = current
        current = nxt

    return prev

if __name__ == '__main__':

#!/bin/python3

import os
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

# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
#
"""
문제: 주어진 테스트케이스만크 두개의  리스트를 비교하여 
      리스트두개가 같으면 1, 다르면0 
      해결방법:  head 와 같이 같으면 계속 다음 엘리멘트를 비교한다. 
                계속 비교하다 마지막까지 비교하여 null 을 찾게되면 1
                중간에 엘리리멘트가 다르게되면 0 을 반환한다. 

input 값 해석 
2   # test case 횟수 
2   # 1번째 test 에서 1번째 list  크기   
1   # 1번째 test 에서 1번째 list  의 1번째 엘리먼트 
2   # 1번째 test 에서 1번째 list  의 2번째 엘리먼트 
1   # 1번째 test 에서 2번째 list  크기   
1   # 1번째 test 에서 2번째 list  의 1번째 엘리먼트  
2   # 2번째 test 에서 1번째 list  크기
1   # 2번째 test 에서 1번째 list  의 1번째 엘리먼트 
2   # 2번째 test 에서 1번째 list  의 2번째 엘리먼트  
2   # 2번째 test 에서 2번째 list  크기
1   # 2번째 test 에서 2번째 list  의 1번째 엘리먼트 
2   # 2번째 test 에서 2번째 list  의 2번째 엘리먼트 

#sample input 
2
2
1
2
1
1
2
1
2
2
1
2

#sample output
0
1
"""
def compare_lists(llist1, llist2):
    node_a = llist1
    node_b = llist2
    while True:
        if not node_a and not node_b:
            return 1
        elif (node_a and node_b) and (node_a.data == node_b.data):
            node_a = node_a.next
            node_b = node_b.next
        else:
            return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        result = compare_lists(llist1.head, llist2.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

"""
문제: 입력된 linked list 에 처클이 존재하면 true, 없으면 false 를 return 하라. 
문제 해설: 입력된 linked list는 단방향 리스트로 빈값일경우 None이다. 
          한개노드일경우 써클이 될수없다. 따라서 False
          
접근 방법: 단방향linked list 이기때문에  2개이상의 노드가 필요.
          써클의 간격을 1개 이상의 노드가 존재할수있다. 
          써클을 확인하기 위해 두개의 속도가 다른 달리기 선수가 있다고 가정 
          
           slow  : 1개 node 씩만 이동하는 하는선수  
           fast  : 2개 node 씩 이동하는 선수 
- 써클안에서 달린다면 두선수는 어느순간 만나는 지점이 존재할것이다. 
- 써클이 없다면 fast 가 linked list를 다  달려서 null  을 만날것이다. (fast.next 가 null 만날때까지 ) 

예시 input:

1-> null  
1-> 2- > 3 -> 2 


예시 output: 
0
1 
          
"""

def has_cycle(head):
    pass

    if (head == None):
        return 0
    else:
        slow = head
        fast = head.next
        while (slow != fast) :
            if (fast == None or fast.next == None):
                return 0
            else:
                slow = slow.next;
                fast = fast.next.next;
        return 1
        

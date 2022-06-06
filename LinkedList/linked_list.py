# Deletion and Insertion is faster in LL compared to array/List
# Search is faster in array/List

# Applications of Linked List
"""
1. Worst case insertion at the begin and end are theta(1) i.e constant time
2. Worst case deletion from the beginning theta(1)
3. Insertion and deletion in the middle are theta(1) if we have reference to the previous node
4. Round robin implementation
5. Merging 2 sorted linked lists is faster than arrays
6. Implementation of simple memory manager where we need to link free blocks
7. Easier implementation of queue and Deque data structures
*/"""

class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print(head)
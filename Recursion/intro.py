"""
A function is called recursive if it calls itself directly or indirectly.

def fun(....):
    Base cases...........
    ..................
    .................

    Recursive call (i.e., call to function(..))
    with at least one change to parameter
    so that call approaches towards the base case

Applications of Recursion:
=========================
1. Many algorithm techniques are based on recursion
    * Dynamic programming
    * Backtracking
    * Divide and Conquer (Binary search, quick sort and merge sort)

2. Many problems inherently recursive
    * Tower of Hanoi
    * DFS based traversals(DFS of graph and inorder/preorder/postorder traversal of tree)
"""
def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
    print(n)

fun(3)

def fun1(n):
    if n <= 0:
        return
    print("GFG")
    fun1(n-1)


fun1(5)

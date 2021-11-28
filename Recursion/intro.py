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
    if n == 0:
        return
    print(n * '*')
    fun(n - 1)
    print(n * '*')


# fun(3)

def fun1(n):
    if n <= 0:
        return
    print("GFG")
    fun1(n - 1)


# fun1(5)


def fun2(n):
    if n <= 1:
        return 0
    else:
        return 1 + fun2(n / 2)


# fun2(16)


def fun3(n):
    if n == 0:
        return
    fun3(n / 2)
    print(n % 2)


# fun3(13)

# Print N to 1 using recursion in python
def fun4(n):
    if n <= 0:
        return
    print(n)
    fun4(n - 1)


# fun4(5)


# Print 1 to N using recursion in python
def fun5(n):
    if n <= 0:
        return 0
    fun5(n - 1)
    print(n)


# fun5(15)

# sum of natural numbers using recursion
def sumOfNaturalNumbers(n):
    if n == 0:
        return 0
    result = result + sumOfNaturalNumbers(n-1)
    return result

# Sum of digits using recursion

def sumOfDigits(n):
    if n <= 9:
        return n
    return sumOfDigits(n // 10) + ( n % 10)


print(sumOfDigits(294))

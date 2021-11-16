"""
Hashing is mainly used to implement dictionaries where you have key-value pairs. After array , second most used DS.
It is also used to implement sets, where you have only keys.
Biggest advantage of hashing is , it provides search, insert and delete all 3 operations in O(1) on an average.

For array ,you have O(n) for search, O(n) for insert, O(n) time for delete if your data is stored in sorted way.
for un-sorted array, delete and insert becomes O(1) and search becomes O(n).

For Binary search trees specially AVL tree and Red-Black Tree,
    O(log n) - search, insert and delete

Hasing is good for exact search .It is not suitable for comparison operations. BST is best in such cases.
Also not suitable for printing sorted order .

Not useful for : --> Finding closest value, -- Best AVL or RedBlack tree
                 --> Sorted data            -- Best AVL or RedBlack tree
                 --> Prefix searching       -- Trie [Alternate dictionary implementation]
"""

"""
Applications of hashing:
=======================
1. Dictionaries
2. Database Indexing
3. Cryptography
4. Caches
5. Symbol tables in compilers/interpreters
6. Routers
7. Getting data from databases
and many more

How hash function works?
=======================
-> Should always map a large key to same small key
-> should generate values from 0 to m-1
-> should be fast, O(1) for integers and O(len) for strings of length 'len'
-> should uniformly distribute large keys into hash table slots

Hash table size depends on the number of entries you have. it is always proportional to them.
Hash function converts those entries into indexes which are used in your hash table.

Example hash functions:
======================
1. h(large_key) = large_key % m. For value of m, we mostly choose prime numbers which are not close to powers
2. For strings, weighted sum is used to avoid permutation problem.
    str[] = "abcd"
    ( str[0] * x^0 + str[1] * x^1 + str[2] * x^2 + str[3] * x^4 ) % m, where m is your table size
3. Universal hashing
"""

"""
Collision handling
=================
when you universe is big, hash table is small. 
So its likely that two keys from your big universe may map to same key in the hash table which results in collision.
Collision is bound to happen if you do not know keys in advance.

Birthday paradox says that if there are 23 people in a room, then there is 50% probability that 2 people 
have same birthday . If the number of people are 70, then the 99.9% probability.

If we know keys in advance, then we can do perfect hashing.
If we do not know keys, then we do one of the following:
    --> chaining
    --> Open Addressing:
            --> Linear probing (Linearly search for next empty slot)
            --> Quadratic probing
            --> Double hashing

** Chaining **
==================
hash(key) = key%7
keys = [50, 21, 58, 17, 15, 49, 56, 22, 23, 25]

Hash Table(Array of Linked List headers)
Linked List is used as whenever any collision happens , we enter the an item at the ned of the LL.
To choose a key, we pick up a value greater than n and closest to n.

 |----------|	
0|	21	    | --> 49 --> 56
 |----------|
1|	50	    | --> 15 --> 22
 |----------|
2|	58	    | --> 23
 |----------|
3|	17	    | 
 |----------|
4|	25	    |
 |----------|
5|		    |
 |----------|
6|		    |
 |----------|
7|		    |
 |----------|

Performance of chaining:
=======================
m = No. of slots in hash table
n = No. of keys to be inserted

Load factor α = n/m

Expected chain length = α
Expected time to search/insert/delete = O(1+α)

Data structures for storing chains:
=================================
Linked List - Search/Insert/Delete O(l). Not cache friendly, extra space
Dynamic sized arrays (vector in c++, ArrayList in Java, list in Python) - Search/Insert/Delete O(l). Cache friendly
Self Balancing BST (AVL Tree, redBlack Tree) - Search/Insert/Delete O(log l). Not cache friendly


"""

"""
                            Chaining vs Open Addressing
                            ==========================
                            
1. Hash table never fills                   Table may become full and resizing becomes mandatory
2. Less sensitive to hash functions         Extra care required for clustering
3. Poor cache performance                   Cache friendly                         
4. Extra space for links                    Extra space might be needed to achieve same performance as chaining
5. Can be used for unknown no. of keys      Can be used when you know number of keys in advance
6. Better version of collision handling
7. Better performance


"""
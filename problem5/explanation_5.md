# Explanation

The Node class stores properties timestamp, data, previous hash, hash and next.

It has some getters and setters to prevent people changing the properties after creation.

Adding a new block consists of walking to the end of the list, and creating the new block at the end.

# Analysis

Add a new node is O(n) because we need to traverse the list in one direction.

Storage is also O(n).




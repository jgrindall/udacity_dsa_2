# Explanation

To find the union and intersection of two linked lists I sort them first.

Once the two lists are sorted the union/intersection algorithms become very simple.

Store two pointers into the lists, check what values they point at and 

* for union, we add the smallest one while we can and advance the pointer when we can't add any more.
We need to check any left-overs too.

* for intersection we just advance the smallest valued pointer and add when our values are equal
There is no need to check left overs, since they will definitely not be in both lists.

# Analysis

Sorting the two lists is O(n log n).

Scanning the lists using the above ideas is O(n).

So the algorithm is O(n log n) overall.

In terms of storage it is O(n) - because copies of the lists are made.


# Explanation

I use a MinHeap to store the nodes.

Once all the work is done making the MinHeap class, it becomes simple to get the least-frequency nodes and to re-insert nodes when building the Huffman tree.

The implementation of the MinHeap is a direct translation from TypeScript to Python of a Heap implementation I wrote for another course:
https://github.com/jgrindall/coursera_algorithms/blob/master/course2/heap/Heap.ts



# Analysis

For the MinHeap, inserting a node is O(log n) and removal is O(1).

If input_string has length n, getting the frequencies of each letter is O(n).

Inserting 'n' elements into the min heap is going to take roughly log(1) + log(2) + ... + log(n) time

Which is log(n!) or about O(n log n)

(See https://www.johndcook.com/blog/2010/08/16/how-to-compute-log-factorial/)

Building the tree is O(n) because we do a search on the entire tree, visiting each node once.

So overall, building the Huffman tree is O(n log n)

In terms of storage, we need O(n) for the tree and O(n) for the encoding table.

--

For decoding and encoding we need to look at the compression ratio.

If we assume a 'typical' situation where all characters have equal frequency we will have an encoding where all characters are encoded with 'm' bits.

All leaf nodes are at level 'm' of the tree, so 2^m = n

This means that m = O(log n)

--

If you encode a message of length 'k', the time complexity is O(k) because we simply use the lookup table.

Each character will be encoded with 'm' bits, so the storage is O(km) = O(k log n)

Eg.

H -> m bits
E -> m bits
L -> m bits
L -> m bits
0 -> m bits

--

If you decode a message of length 'k' bits, you will get a decoded message of length 'k/m'


m bits -> H
m bits -> E
m bits -> L
m bits -> L
m bits -> O


For each letter we traverse 'm' levels of the tree, so for (k/m) letters we will do (k/m)*m steps, which is O(k)

The additional storage needed is O(k/m) = O(k/log n)


# Explanation


'_find_files' iterates through the folder, checking files and calling itself recursively on any subdirectories.

I have not dealt with symlinks which could cause circular loops.

This would be easy to do by storing a dict mapping paths to whether they have been checked already.

# Analysis


In terms of time complexity, we traverse all files, which is O(N) where N is the total number of files.

In terms of storage, we store the array 'entries' in each recursive call.

Suppose there are 'n' files and folders in each directory, and that the tree is 'k' levels deep.

The call stack will be a maximum of 'k' levels deep at any time.

So we need O(kn) memory.

Plus an additional worst case O(N) to store the returned array of matching files.


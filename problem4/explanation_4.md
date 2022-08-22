# Explanation


'_is_user_in_group' iterates through the users, checking if the user is found.

If not, it checks each sub-group of the group.

I believe Active Directories can contain loops (https://www.rlmueller.net/CircularNested.htm) so I mark each group with a status 'in progress' or 'done' as it is searched.

Any non-null status means that the group is skipped.


# Analysis


In the worst case the algorithm will require O(n) steps to find the user, where n represents the total number of users.

The code requires no additional storage other than that which already holds the AD tree, other than the 'checked_groups' dict which is O(g) where g is the number of groups.



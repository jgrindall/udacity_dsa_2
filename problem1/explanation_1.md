# Explanation


'self.dict' maps keys to Nodes (note: not values)

Eg. self.dict = { 1 -> Node(key = 1, value = "apple"), 2 -> Node(key = 2 , value = "banana") }

The value for 'key' is looked up as 'self.dict[key].value'

Additionally, a doubly linked list of nodes is maintained:


oldest_node -> (next) -> node -> (next) -> node -> (next) -> node -> (next) -> newest_node

oldest_node <- (prev) <- node <- (prev) <- node <- (prev) <- node <- (prev) <- newest_node


When the value of an existing key is changed, and when the value is accessed, that node is moved to become the newest_node and the list is re-linked appropriately.

When a new value is added it becomes newest_node and if the cache has reached capacity, oldest_node is removed.

These structures allow fast lookup at the expense of having to maintain a doubly linked list.

# Analysis


Using the dict means that accessing a key's value is O(1).

Setting the value of a key is O(1).

The structures are O(n) in terms of storage space.
class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None

    def __repr__(self):
        return "Node:{0} -> {1}".format(self.key, self.value)
     
    def __str__(self):
         return self.__repr__()


class LRUCache(object):
    def __init__(self, capacity):
        # maps keys to nodes. Eg..{ 1 -> Node(1, "apple"), 2 -> Node(2, "banana") }
        self.dict = {}

        # a doubly linked list of nodes
        self.oldest_node = None
        self.newest_node = None

        self.current_size = 0
        self.capacity = capacity

    def get(self, key):
        if key in self.dict:
            node = self.dict[key]
            self.__set_used(key)
            return node.value
        return -1

    def get_empty(self):
        return self.current_size == 0

    def __set_used(self, key):
        """Private function to promote a node to be the 'most recently used/newest'"""
        node = self.dict[key]
        # it's already the newest one, ignore
        if node is self.newest_node:
            return
        else:
            # make it the newest one.
            
            # first, store the current newest node
            current_newest_node = self.newest_node
            # and the node that will be the new oldest
            new_oldest_node = self.oldest_node.next
            
            # next take out the node and re-connect its neighbours
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            
            # and finally add the node to the end
            current_newest_node.next = node
            node.prev = current_newest_node
            node.next = None
            self.newest_node = node
            self.oldest_node = new_oldest_node

    def __add(self, key, value):
        """It doesnt exist, we need to add it."""
        
        # First make a new node
        node = Node(key, value)
        
        # if empty
        if self.get_empty():
            self.dict[key] = node
            self.oldest_node = node
            self.newest_node = node
            self.current_size = 1
            
        else:
            def add(node):
                """Helper function -just adds a node to the end"""
                current_newest_node = self.newest_node
                current_newest_node.next = node
                node.prev = current_newest_node
                self.newest_node = node
                self.dict[key] = node
    
            if self.current_size < self.capacity:
                # if there is spare capacity, just add it. it will become the newest one and increase the size by 1
                add(node)
                self.current_size += 1
            else:
                # we reached capacity, remove oldest, add newest, and do not change the size
                add(node)
                new_oldest_node = self.oldest_node.next
                new_oldest_node.prev = None
                del self.dict[self.oldest_node.key]
                self.oldest_node.next = None
                self.oldest_node = new_oldest_node
               

    def set(self, key, value):
        # it already exists, just set the value and call 'set used'
        if key in self.dict:
            node = self.dict[key]
            self.__set_used(key)
            node.value = value
            
        else:
            self.__add(key, value)
    
    def to_list(self):
        """ for printing """
        entries = []
        node = self.oldest_node
        while node:
            entries.append([node.key, node.value])
            node = node.next
        return entries
    
    def __repr__(self):
        """ for printing """
        return "LRUCache:" + str(self.to_list())
     
    def __str__(self):
         return self.__repr__()


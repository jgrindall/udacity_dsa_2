class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return "Node:{0}".format(self.value)
     
    def __str__(self):
         return self.__repr__()

class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        my_list = []
        node = self.head
        while node:
            my_list.append(node.value)
            node = node.next
        return my_list
    
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
    
    def get_sorted(self):
        """ return a shallow clone, sorted """
        to_list = self.to_list()
        sorted_list = sorted(to_list)
        return LinkedList.from_list(sorted_list)
        
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return "LinkedList " + str([v for v in self])
    
    def __str__(self):
        return self.__repr__()

    @staticmethod
    def from_list(list):
        """Helper function, make a new LinkedList"""
        new_list = LinkedList()
        for item in list:
            new_list.append(item)
        return new_list


class SetUtils:
    @staticmethod
    def union(l1, l2):
        union = []
        
        #sort them first and then the algorithm will be much simpler
        s1 = l1.get_sorted()
        s2 = l2.get_sorted()
        
        node1 = s1.head
        node2 = s2.head
        
        last_value = None
        
        def add(value):
            # add if it doesn't exist already - this will remove duplicates
            nonlocal last_value
            if last_value != value:
                union.append(value)
                last_value = value
        
        while node1 and node2:
            #add the smallest one while we can
            if node1.value < node2.value:
                add(node1.value)
                node1 = node1.next
            elif node1.value > node2.value:
                add(node2.value)
                node2 = node2.next
            else:
                #equal  -advance both
                add(node1.value)
                node1 = node1.next
                node2 = node2.next
        
        # do any remaining items. Note that not both of these will run
        while node2:
            add(node2.value)
            node2 = node2.next
        while node1:
            add(node1.value)
            node1 = node1.next
        return LinkedList.from_list(union)


    @staticmethod
    def intersection(l1, l2):
        intersection = []
        s1 = l1.get_sorted()
        s2 = l2.get_sorted()
        
        node1 = s1.head
        node2 = s2.head
        
        last_value = None
        
        def add(value):
            # add if it doesn't exist already
            nonlocal last_value
            if last_value != value:
                intersection.append(value)
                last_value = value
        
        while node1 and node2:
            # go forward without adding until they are equal
            if node1.value < node2.value:
                node1 = node1.next
            elif node1.value > node2.value:
                node2 = node2.next
            else:
                #equal
                add(node1.value)
                node1 = node1.next
                node2 = node2.next
        
        # no need to do any remaining items.
        return LinkedList.from_list(intersection)



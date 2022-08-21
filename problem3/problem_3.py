import random

class Node:
    def __init__(self, value, data = None):
        self.value = value
        self.left = None
        self.right = None
        self.data = data
        

    def __gt__(self, other):
        return self.value > other.value

    def __repr__(self):
        s = "Node:" + str(self.value)
        if self.data is not None:
            s += " data " + str(self.data)
        if self.left:
            s += " left " + str(self.left)
        if self.right:
            s += " right " + str(self.right)
        return s
     
    def __str__(self):
         return self.__repr__()



class MinHeap:
    def __init__(self, elements = []):
        self.elements = []
        if len(elements) >= 1:
            self.elements.append(elements[0])
        for element in elements[1:]:
            self.insert(element)
        
    def __swap(self, i, j):
        t = self.elements[i]
        self.elements[i] = self.elements[j]
        self.elements[j] = t

    def __get_child_indices(self, i):
        return [
            2*i + 1,
            2*i + 2
        ]

    def get_size(self):
        return len(self.elements)

    def __get_parent_index(self, i):
        return (i - 1)//2
    
    def __get_children(self, i):
        children = []
        num_elements = self.get_size()
        for index in self.__get_child_indices(i):
            if index <= num_elements - 1:
                children.append(self.elements[index]);
        return children
    
    def is_valid(self):
        for i in range(self.get_size()):
            if not self.__check_heap_property(i):
                return False
        return True
    
    def __check_heap_property(self, index):
        elt = self.elements[index]
        children = self.__get_children(index)
        incorrect_children = list(filter(lambda child: elt > child, children))
        return len(incorrect_children) == 0;
    
    def insert(self, node):
        current_len = len(self.elements)
        self.elements.append(node)
        index = current_len
        parent_index = self.__get_parent_index(index)
        while parent_index >= 0 and not self.__check_heap_property(parent_index):
            # bubble up
            self.__swap(index, parent_index)
            index = parent_index
            if parent_index == 0:
                # we have set the root
                parent_index = -1
            else:
                parent_index = self.__get_parent_index(parent_index)
        
    def get(self):
        num_elements = self.get_size()
        if num_elements == 0:
            return None
        return self.elements[0]
    
    def remove(self):
        num_elements = self.get_size()
        if num_elements == 0:
            return None
        else:
            root = self.elements[0]
            last = self.elements[-1]
            self.elements[0] = last
            self.elements.pop()
            if len(self.elements) == 0:
                return root
            else:
                # bubble down
                index = 0;
                while not self.__check_heap_property(index):
                    children = self.__get_children(index);
                    if len(children) == 0:
                        raise ValueError("heap property failed");
                    else:
                        child_index = None
                        num_children = len(children)
                        if num_children == 1 or (num_children == 2 and children[0] < children[1]):
                            # left child
                            child_index = self.__get_child_indices(index)[0]
                        else:
                            # right child
                            child_index = self.__get_child_indices(index)[1]
                        self.__swap(index, child_index)
                        index = child_index
                return root
        
    def __repr__(self):
        return "MinHeap:" + str(self.elements)
     
    def __str__(self):
         return self.__repr__()



class Huffman:
    

    def __init__(self, input_string):
        chars = list(input_string)
        weights = {}
        for char in chars:
            if char in weights:
                weights[char] += 1
            else:
                weights[char] = 1
                
        self.heap = MinHeap()
        for char in weights:
            self.heap.insert(Node(weights[char], {"char": char}))
        
        while self.heap.get_size() >= 2:
            node0 = self.heap.remove()
            node1 = self.heap.remove()
            new_char =  node0.data["char"] + node1.data["char"]
            new_value = node0.value + node1.value
            new_node = Node(new_value, {"char": new_char})
            new_node.left = node0
            new_node.right = node1
            self.heap.insert(new_node)

        self.encoding = {}
        self.tree = self.heap.elements[0]
        
        current_path = []
        def visit(node):
            if not node.left and not node.right:
                #leaf
                letter = node.data["char"]
                self.encoding[letter] = "".join(current_path)
            if node.left:
                current_path.append('0')
                visit(node.left)
            if node.right:
                current_path.append('1')
                visit(node.right)
            if len(current_path) >= 1:
                current_path.pop()
        visit(self.tree)
    
    def get_encoding_table(self):
        return self.encoding
    
    def get_huffman_encoding(self, msg):
        encoded = ""
        for char in msg:
            encoded += self.encoding[char]
        return encoded
    
    def get_huffman_decoding(self, bytes):
        decoded = ""
        root = self.tree
        
        #reverse so we can pop
        bytes_reversed = list(bytes)[::-1]
        
        def find_letter(start_node):
            if not start_node.left and not start_node.right:
                #leaf
                return start_node.data["char"]
            elif len(bytes_reversed) == 0:
                return None
            else:
                byte = bytes_reversed.pop()
                if byte == "0":
                    return find_letter(start_node.left)
                else:
                    return find_letter(start_node.right)

        while True:
            letter = find_letter(root)
            if not letter:
                break
            else:
                decoded += letter
        
        return decoded

    def get_tree(self):
        return self.tree





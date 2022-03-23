# Class for a generic linked list
class Node():
    """
    Models a node in a linked list with functionality for doubly or singly linked
    """

    def __init__(self, data):
        """
        data: node value, any type
        """
        self.data = data
        self.child = None
        self.parent = None

    def get_parent(self):
        return self.parent

    def get_child(self):
        return self.child

    def get_data(self):
        return self.data

    def set_parent(self, node):
        self.parent = node

    def set_child(self, node):
        self.child = node

    def set_data(self, data):
        self.data = data

    def add_to_head(self, value):
        new_node = Node(value)
        self.parent = new_node
        new_node.child = self

    def add_to_tail(self, value):
        new_node = Node(value)
        self.child = new_node
        new_node.parent = self

    def __repr__(self):
        return f"<Node>: Value = {self.data}"

class LinkedList():
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def add_to_head(self, node):
        if self.head:
            node.child = self.head
            self.head.parent = node
            self.head = node
        else:
            self.head = node
            self.tail = node

    def add_to_tail(self, node):
        if self.tail:
            self.tail.child = node
            node.parent = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def delete(self, value):
        """
        Deletes first instance of value, returns -1 if value not in linked list
        """
        if self.tail.data == value and self.head.data != value:
            self.tail.parent.child = None
            self.tail = self.tail.parent

        current = self.head
        while current:
            if current.data == value:
                if current.parent:
                    current.parent.child = current.child
                else:
                    self.head = self.head.child
                if current.child:
                    current.child.parent = current.parent
                current.parent = None
                current.child = None
                break
            else:
                current = current.child

            if current.child == None:
                # return -1
                raise IndexError(f"{value} not in liked list")

    def index(self, value):
        """ Returns index of value. Returns -1 in value not in linked list. Alt: Prints not in list"""
        if self.head:
            current = self.head
        else:
            # return -1
            return "f{value} not in linked list"
        count = 0
        while True:
            if current.data == value:
                return count
            elif current.child:
                count += 1
                current = current.child
            else:
                # return -1
                return "f{value} not in linked list"


    def __repr__(self):
        rep = []
        if self.head:
            current = self.head
        else:
            return "Linked list empty"
        while current.child:
            rep.append(current)
            current = current.child
        rep.append(self.tail)
        return f"{rep}"



# Example Usage
N1 = Node(10)
N2 = Node(20)
N3 = Node(30)
N4 = Node(25)

LL = LinkedList()
LL.add_to_head(N1)
LL.add_to_head(N2)
# LL.add_to_head(N2)
LL.index(10)
print(LL, "\n", N1, N2, N3, N4, "\n", LL.index(10))







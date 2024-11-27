class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data
    
    
class LinkedList:
    """ Singly Linked list"""
    head = None

    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def size(self):
        """ Returns the number of nodes in list """
        current = self.head
        count = 0

        while current:
            count +=1
            current = current.next_node
        return count
    
    def add(self,data):
        """ adds a new node containing data at head of the list"""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self,key):
        """ Seach for the first node containing data that matches the key """
        current = self.head
        position = 0
        while current:
            position += 1
            if current.data == key:
                return f"found at position : {position}"
            else:
             current = current.next_node
        return "not found"
    
    def display(self):
        current = self.head
        while current:
                print(current.data, end=' -> ')
                current = current.next_node
            


if __name__ == "__main__":
    l = LinkedList()
    l.add(1)
    l.add(5)
    l.add(3)
    print(l.size())
    print(l.display())
    print(l.search())


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LList:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        if(self.head == None):
            return "Linked List is empty"
        else:
            return "Linked List is not empty"

    # Add at the last
    def appendNode(self, new_node):
        current = self.head # The head of the linked list is the current most data
        
        if current: # If true or current exists or the linked list is not empty
            while current.next:
                current = current.next # Keep going till the end
            
            current.next = new_node # Assign the tail the value of new_node. Hence we append this
        
        else:
            self.head = new_node # If the current.next is empty / false, i.e it's empty then assign the tail the value of new_node

    def appendData(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prependData(self, value):
        new_node = Node(value) # Node(value) is another good way of doing this
        new_node.next = self.head # The new node is now set to the head
        self.head = new_node # we added the new_node on top of the head


    def prependNode(self, new_node):
        new_node.next = self.head # The new_node is pointing to the node head i.e we added on top of other head
        self.head = new_node # Update the head to be the new_node

    """
        
    1 -> 2 -> 3 -> None
    ^
    |
    head
    """

    """
    1 -> 2 -> 3 -> None
    ^
    |
    new_node -> (points to the original head)
    """

    # Create the iterator
    def __iter__(self):
        self.current_node = self.head
        return self
    
    # Define the behaviour of the iterator
    def __next__(self):
        if self.current_node:
            value = self.current_node.value # Get the value
            self.current_node = self.current_node.next # Pass the pointer
            return value # Return the value
        
        else: # If the linked list is empty
            raise StopIteration
        

# Creating the nodes

e1 = Node("204")
e2 = Node(304)
e3 = Node("g7834uyrwhj")
e4 = Node("999999999999")

linked_list = LList(e1)
linked_list.appendNode(e2) # Append to e1
linked_list.appendNode(e3) # Append to e1

linked_list.appendData(100)
linked_list.appendData("yieuhdiuh")

linked_list.prependNode(e4)

# Print using the iterator
for i in linked_list:
    print(i)
            

# f1 = Node(98)
# linked_list = LList()
# print(linked_list.is_empty())
# linked_list = LList(f1)
# print(linked_list.is_empty())



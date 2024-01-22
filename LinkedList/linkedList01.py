# Giving the linked list some basic function

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        current = self.head

        if current:
            while current.next:  # While current.net returns exist because it exists
                current = current.next # Go until the end of the linked list
            # At the end, just add the new_node    
            current.next = new_node

        else: # that is it's false and the node was already empty. So just chain this
            self.head = new_node


if __name__ == "__main__":
    e1 = Node(30)
    linked_list = LList(e1)
    for element in linked_list:
        print(element)
    
"""
Traceback (most recent call last):
  File "/Users/axjh03/MEGAsync/PythonDSA/LinkedList/linkedList01.py", line 29, in <module>
    for element in linked_list:
    
### TypeError: 'LList' object is not iterable

"""


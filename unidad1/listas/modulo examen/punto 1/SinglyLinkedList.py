from Node import Node

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def __str__(self) -> str:
        current_node = self.head
        list_str = '[ '
        while current_node:
            list_str += f'{current_node} '
            current_node = current_node.next_node
        return list_str + ']'

    def has_something(self) -> bool:
        return self.size > 0

    def prepend(self, value) -> None:
        """Append object to the beginning of the list."""
        new_node = Node(value)
        if self.head == None: # If the list is empty
            self.head = new_node
            self.size += 1 # The size of the list increases
        else:
            # The list has at least one node
            new_node.next_node = self.head
            self.head = new_node # Update the first node
            self.size += 1

    def append(self, value) -> None:
        """Append object to the end of the list."""
        new_node = Node(value)
        if self.size == 0:
            self.head = new_node
            self.size += 1
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node
            self.size += 1

    def object_is_in(self, value) -> bool:
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False

    def append_or_preppend(self, value) -> None:
        """Add a value, taking into account that if the data already
        exists in the list, it is added to the end of the list; if it
        doesn't exist, it is added to the beginning of the list
        """
        if self.object_is_in(value) == True:
            self.append(value)
        else:
            self.prepend(value)

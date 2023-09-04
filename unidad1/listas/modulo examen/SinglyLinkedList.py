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
            self.head   = new_node
            self.size  += 1 # The size of the list increases
        else:
            # The list has at least one node
            new_node.next_node = self.head
            self.head   = new_node # Update the first node
            self.size  += 1

    def append(self, value) -> None:
        """Append object to the end of the list."""
        new_node = Node(value)
        if self.size == 0:
            self.head   = new_node
            self.size  += 1
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node
            self.size += 1

    def delete_first(self) -> None:
        """Delete the first object in the list."""
        if self.has_something():
            second_node = self.head.next_node
            self.head = second_node
            self.size -= 1

    def delete_last(self) -> None:
        """Delete the last object in the list."""
        if self.has_something():
            if self.size == 1:
                self.head = None
            else:
                current_node = self.head
                previous_node = self.head
                while current_node.next_node:
                    previous_node = current_node
                    current_node = current_node.next_node
                previous_node.next_node = None
            self.size -= 1

    def delete_index(self, index) -> None:
        """Delete the element at the given index."""
        try:
            assert index >= 0, 'Index out of range'
            assert index <= self.size-1, 'Index out of range'
        except AssertionError as error:
            return error
        current_index = 0
        current_node = self.head
        previous_node = self.head
        if self.has_something():
            while current_node.next_node:
                if current_index == index:
                    previous_node.next_node = current_node.next_node
                    self.size -= 1
                    break
                previous_node = current_node
                current_node = current_node.next_node
                current_index += 1

    def count(self, value) -> int:
        """Count the number of times the value appears in the list."""
        counter = 0
        if self.has_something():
            current_node = self.head
            while current_node:
                if current_node.value == value:
                    counter += 1
                current_node = current_node.next_node
        return counter

    def find(self, index):
        """Find the element at the given index."""
        try:
            assert index >= 0, 'Index out of range'
            assert index <= self.size-1, 'Index out of range'
        except AssertionError as error:
            return error
        current_index = 0
        current_node = self.head
        if self.has_something():
            while current_node.next_node:
                if current_index == index:
                    return current_node
                current_node = current_node.next_node
                current_index += 1

    def where_is(self, object) -> 'SinglyLinkedList':
        """Return a list containing the indices of the given object."""
        indices = SinglyLinkedList()
        current_index = 0
        current_node = self.head
        while current_node:
            if current_node.value == object:
                indices.append(current_index)
            current_node = current_node.next_node
            current_index += 1
        return indices

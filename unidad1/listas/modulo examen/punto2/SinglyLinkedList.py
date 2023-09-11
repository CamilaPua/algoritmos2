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
    
    def __iter__(self):
        self.current_node = self.head
        return self

    def __next__(self):
        if self.current_node:
            value = self.current_node.value
            self.current_node = self.current_node.next_node
            return value
        else:
            raise StopIteration

    def object_is_in(self, value) -> bool:
        for node in self:
            if node == value:
                return True
        return False

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

    def delete(self, object):
        current_node = self.head
        previous_node = self.head
        while current_node:
            if current_node.value == object:
                if current_node == self.head:
                    self.head = current_node.next_node
                else:
                    previous_node.next_node = current_node.next_node
                self.size -= 1
                break
            previous_node = current_node
            current_node = current_node.next_node

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
            while current_node:
                if current_index == index:
                    if self.size == 1 or current_node == self.head:
                        self.head = current_node.next_node
                    else:
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

    def find_penultimate(self):
        """Return the penultimate object of the list."""
        if self.size <= 1:
            return 'There is no penultimate object'
        else:
            current_node = self.head
            previous_node = self.head
            while current_node.next_node:
                previous_node = current_node
                current_node = current_node.next_node
            return previous_node

    def slice_between(self, start: int, end: int):
        """Indicate the elements between two positions of the list.
        start and end, where start < end 
        """
        try:
            assert end <= self.size, 'Index out of range.'
            assert start >= 0, 'Index out of range.'
            assert start < end, 'The initial position must be less than the final position.'
        except AssertionError as error:
            return error
        current_node = self.head
        current_index = 0
        between_elements = SinglyLinkedList()
        while current_node:
            if current_index > start and current_index < end:
                between_elements.append(current_node)
            current_node = current_node.next_node
            current_index += 1
        return between_elements

    def clean_this_data(self, object):
        """Remove all occurrences of a data item from the list."""
        try:
            assert self.size > 0, 'The list is empty'
        except AssertionError as error:
            return error
        current_node = self.head
        previous_node = self.head
        while current_node:
            if current_node.value == object:
                if current_node == self.head:
                    self.head = current_node.next_node
                    self.size -= 1
                else:
                    previous_node.next_node = current_node.next_node
                    self.size -= 1
            previous_node = current_node
            current_node = current_node.next_node
        # indices = self.where_is(object)
        # print(indices)
        # for index in indices:
        #     print(self.delete_index(index))

    def compare(self, other_list):
        """Determine if two lists are equal in length and content (element order)."""
        return str(self) == str(other_list)

    def object_is_in(self, value) -> bool:
        current_node = self.head
        if self.has_something():
            while current_node:
                if current_node.value == value:
                    return True
                current_node = current_node.next_node
        return False

    def remove_common(self, other_list):
        """Remove common elements between two lists."""
        common_elements = SinglyLinkedList()
        for i in self:
            if other_list.object_is_in(i):
                common_elements.append(i)
        for element in common_elements:
            while self.object_is_in(element) or other_list.object_is_in(element):
                other_list.delete(element)
                self.delete(element)

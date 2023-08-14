from Node import Node

# Singly linked list class
class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def list_is_empty(self):
        return self.head == None

    def append_at_beginning(self, data):
        new_node = Node(data)
        if self.list_is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head     = new_node    # Update list head

    def __str__(self) -> str:
        route = '[ '
        current_node = self.head
        while current_node != None:
            route += str(current_node) + ' '
            current_node = current_node.next
        return route + ']'


if __name__ == '__main__':
    pass

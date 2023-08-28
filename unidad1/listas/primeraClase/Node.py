# Single node class
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


    def __str__(self) -> str:
        return str(self.data)


# Double node class
class DoubleNode(Node):
    def __init__(self, data) -> None:
        super.__init__(self, data)
        self.previous = None


if __name__ == '__main__':
    nodo01 = Node('Casa')
    print(f'Nodo: {nodo01}')

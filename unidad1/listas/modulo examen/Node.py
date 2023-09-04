class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next_node = None

    def __str__(self) -> str:
        return str(self.value)

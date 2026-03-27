class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    parts = list_repr.split(" -> ")

    current_node = None

    for i in range(len(parts) - 2, -1, -1):
        current_node = Node(int(parts[i]), current_node)

    return current_node

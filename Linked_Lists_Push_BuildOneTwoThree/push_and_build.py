
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    list_head = None

    list_head = push(list_head, 3)
    list_head = push(list_head, 2)
    list_head = push(list_head, 1)

    return list_head

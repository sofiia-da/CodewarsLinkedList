
class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if index < 0:
        raise IndexError("Index out of range")

    current = node
    counter = 0

    while current is not None:
        if counter == index:
            return current

        current = current.next
        counter += 1
    raise IndexError("Index out of range")

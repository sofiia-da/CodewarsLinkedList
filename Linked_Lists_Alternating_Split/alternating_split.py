class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if not head or not head.next:
        raise ValueError("List must have at least two nodes to split")

    first_samp = Node()
    second_samp = Node()

    curr1 = first_samp
    curr2 = second_samp

    current = head
    count = 0

    while current:
        if count % 2 == 0:
            curr1.next = current
            curr1 = curr1.next
        else:
            curr2.next = current
            curr2 = curr2.next

        current = current.next
        count += 1

    curr1.next = None
    curr2.next = None

    return Context(first_samp.next, second_samp.next)

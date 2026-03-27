class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if not head or not head.next:
        return head

    samp = Node()
    samp.next = head
    current = samp

    while current.next and current.next.next:
        first = current.next
        second = current.next.next

        current.next = second
        first.next = second.next
        second.next = first

        current = first

    return samp.next

def stringify(node):
    res = ''
    while node is not None:
        res += f'{node.data} -> '
        node = node.next
    res += 'None'

    return res
        
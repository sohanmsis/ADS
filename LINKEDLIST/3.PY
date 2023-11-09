class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_sum_of_last_n_nodes(head, n):
    ptr1 = ptr2 = head
    for _ in range(n):
        ptr2 = ptr2.next

    if ptr2 is None:
        return 0

    while ptr2.next is not None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    sum_of_last_n_nodes = ptr1.data

    return sum_of_last_n_nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return head

    # Create an empty set to store visited nodes
    visited = {head.data}

    # Start from the second node
    current = head.next
    previous = head

    while current:
        if current.data in visited:
            # If the node is duplicate, then remove it
            previous.next = current.next
        else:
            # Otherwise, add the node to the set and move on
            visited.add(current.data)
            previous = current
        current = current.next

    return head

# Test the function
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

print("Original linked list:")
print(head.data)
node = head.next
while node:
    print(node.data)
    node = node.next

head = remove_duplicates(head)

print("\nLinked list after removing duplicates:")
print(head.data)
node = head.next
while node:
    print(node.data)
    node = node.next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        """Inserts a new node at the front of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Inserts a new node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        """Recursively sums all node values. Returns 0 if empty."""
        def _sum_recursive(node):
            if node is None:
                return 0
            return node.data + _sum_recursive(node.next)

        return _sum_recursive(self.head)

    def recursive_search(self, target):
        """Recursively searches for a target value. Returns True or False."""
        def _search_recursive(node, target):
            if node is None:
                return False
            if node.data == target:
                return True
            return _search_recursive(node.next, target)

        return _search_recursive(self.head, target)

    def recursive_reverse(self):
        """Recursively reverses the linked list in-place."""
        def _reverse_recursive(current, prev):
            if current is None:
                return prev
            next_node = current.next
            current.next = prev
            return _reverse_recursive(next_node, current)

        self.head = _reverse_recursive(self.head, None)
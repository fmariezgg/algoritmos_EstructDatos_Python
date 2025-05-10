class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self)


class Stack:
    def __init__(self):
        """Create an empty stack"""
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, data):
        """Add an element to the top of the stack (Create)"""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pop(self):
        """Remove and return the top element from the stack (Delete)"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        data = self.tail.data
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return data

    def peek(self):
        """Return the top element without removing it (Read)"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.tail.data

    def update(self, index, new_data):
        """Update an element at a specific position (Update)"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        current = self.head
        for _ in range(index):
            current = current.next
        current.data = new_data

    def is_empty(self):
        """Check if the stack is empty"""
        return self.size == 0

    def __len__(self):
        """Return the size of the stack"""
        return self.size

    def __str__(self):
        """Return a string representation of the stack"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "Empty Stack"


# Example usage
if __name__ == "__main__":
    stack = Stack()

    # Create (push)
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack after pushes:", stack)  # 10 -> 20 -> 30

    # Read (peek)
    print("Top element:", stack.peek())  # 30

    # Update
    stack.update(1, 25)
    print("After updating index 1:", stack)  # 10 -> 25 -> 30

    # Delete (pop)
    print("Popped:", stack.pop())  # 30
    print("Stack after pop:", stack)  # 10 -> 25

    # Check size
    print("Stack size:", len(stack))  # 2
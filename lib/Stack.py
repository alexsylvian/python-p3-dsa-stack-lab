class Stack:
    def __init__(self, initial_data=None, limit=None):
        if initial_data is not None:
            self.items = list(initial_data)
        else:
            self.items = []
        self.limit = limit

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.limit is not None and len(self.items) >= self.limit:
            return  # Do nothing when the stack is full
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

# Bonus Methods

    def size(self):
        return len(self.items)

    def empty(self):
        return self.is_empty()

    def full(self):
        if self.limit is not None:
            return len(self.items) == self.limit
        else:
            return False

    def search(self, value):
        try:
            index = self.items.index(value)
            return len(self.items) - index - 1
        except ValueError:
            return -1
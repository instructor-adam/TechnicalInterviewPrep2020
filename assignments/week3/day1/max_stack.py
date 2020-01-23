class Max_stack:
    def __init__(self):
        self.stack = []
        self._max = 0

    def push(self, entry):
        # Whenever a new number is inserted, it is compared against the stack to see if it is max
        # if it is not, then a new max is retained
        # One possible implementation
        self.stack.append(entry)
        self._max = max(self.stack)

    def pop(self):
        return self.stack.pop(-1)

    def peek(self):
        return self.stack[-1] if len(self.stack) >= 1 else -1

    def max(self):
        return self._max
        # Another possible implementation
        """ max_in_stack = 0
        for num in self.stack:
            if num > max_in_stack:
                max_in_stack = num
        return max_in_stack
        """
class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * self.capacity

    def insert(self, index, value):
        if self.count == self.capacity:
            print("Error: Array is full")
            return
        if index >= self.count:
            # TODO better error handling
            print("Error: Index out of bounds")
            return
        for i in range(self.count, index, -1):
            self.storage[i] = storage[i - 1]

        self.storage[index] = value
        self.count += 1

    def append(self, index, value):
        if self.count == self.capacity:
            print("Error: Array is full")
            return

        self.storage[self.count] = value
        self.count += 1

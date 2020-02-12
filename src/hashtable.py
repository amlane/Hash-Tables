# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return "{" + f"{self.key}: {self.value}" + "}"


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # hash the key
        index = self._hash_mod(key)

        # if the index of storage is None, insert the (key, value) pair at that index
        if self.storage[index] is None:
            self.storage[index] = LinkedPair(key, value)
        # elif the key already exists at the head of LL, replace the value
        elif self.storage[index].key == key:
            self.storage[index].value = value
        else:
            # go to that index of the list
            last_item = self.storage[index]
            # iterate the linked list and check for last items and key matches
            while last_item.next is not None and last_item.key != key:
                last_item = last_item.next
            # if the key matches, replace the value
            if last_item.key == key:
                last_item.value = value
            # otherwise create a new linked pair and set it as the last item
            new_node = LinkedPair(key, value)
            last_item.next = new_node

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # hash the key
        index = self._hash_mod(key)
        item = self.storage[index]
        # if the index is not empty
        if item is not None:
            # and the key matches
            if item.key == key:
                # assign the item's value to None
                item.value = None
            else:
                cur_item = item.next
                while cur_item is not None:
                    if cur_item.key == key:
                        cur_item.value = None
                    cur_item = cur_item.next
                # handle if it's never found
        else:
            print("Key not found")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # hash the key
        index = self._hash_mod(key)
        item = self.storage[index]
        # if the index is not empty
        if item is not None:
            # and the key matches
            if item.key == key:
                # return item at index in storage
                return item.value
            else:
                # print(f"Warning: collision at {index}")
                cur_item = item.next
                while cur_item is not None:
                    if cur_item.key == key:
                        return cur_item.value
                    cur_item = cur_item.next
                # handle if it's never found
        else:
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # save the current hashmap in another temp var
        old_storage = self.storage
        # double the capacity
        self.capacity *= 2
        # set storage back to a list of None's
        self.storage = [None] * self.capacity
        # insert each item that is not None from old storage into storage

        for item in old_storage:
            # if the head is the only item, just insert that one
            if item is not None and item.next is None:
                self.insert(item.key, item.value)
            # if there's a LL, iterate over it and insert each item
            if item is not None and item.next is not None:
                cur_item = item
                while cur_item.next is not None:
                    self.insert(cur_item.key, cur_item.value)
                    cur_item = cur_item.next
                # don't forget the last little guy!
                self.insert(cur_item.key, cur_item.value)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

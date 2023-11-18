class HashTable:
    NONE_TYPE = (None, None)
    KEY = 0
    VAL = 1

    def __init__(self) -> None:
        self.capacity = 10
        self.data = [self.NONE_TYPE] * self.capacity

    # We will implement this using open addressing.
    def put(self, key, value):
        hash_v = hash(key)
        index = hash_v % self.capacity
        if self.data[index] != self.NONE_TYPE:
            new_index = index + 1
            # Naively using linear probing
            while new_index < self.capacity and self.data[new_index] == self.NONE_TYPE:
                new_index += 1
            if new_index == self.capacity:
                raise Exception
            self.data[new_index] = key, value
        else:
            self.data[index] = key, value

    def get(self, key):
        hash_v = hash(key)
        index = hash_v % self.capacity
        maybe_data = self.data[index]

        new_index = index
        while maybe_data[self.KEY] != key:
            new_index += 1
            maybe_data = self.data[new_index]
        if new_index == self.capacity:
            raise Exception
        
        return maybe_data[self.VAL]

    def delete(self, key):
        hash_v = hash(key)
        index = hash_v % self.capacity
        maybe_data = self.data[index]

        new_index = index
        while new_index < self.capacity and maybe_data[self.KEY] != key:
            new_index += 1
            maybe_data = self.data[new_index]
        if new_index == self.capacity:
            raise Exception

        self.data[new_index] = self.NONE_TYPE
        







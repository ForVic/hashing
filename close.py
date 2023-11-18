class ListNode:
    NONE_TYPE = (None, None)
    def __init__(self, val=None, next=None):
        if val == None:
            val = self.NONE_TYPE
        self.val = val
        self.next = next 

class HashTable:
    KEY = 0
    VAL = 1
    EMPTY_NODE = ListNode()
    def __init__(self) -> None:
        self.capacity = 10
        self.data = [self.EMPTY_NODE] * self.capacity

    def put(self, key, val):
        hash_v = hash(key)
        index = hash_v % self.capacity
        if self.data[index] != self.EMPTY_NODE:
            node_ref = self.data[index]
            while node_ref.next != None:
                if node_ref.val[self.KEY] == key:
                    node_ref.val = (key, val)
                    return
                node_ref = node_ref.next
            node_ref.next = ListNode(val=(key, val))
        else:
            self.data[index] = ListNode(val=(key, val))

    def get(self, key):
        hash_v = hash(key)
        index = hash_v % self.capacity
        if self.data[index] != self.EMPTY_NODE:
            node_ref = self.data[index]
            while node_ref != None and node_ref.val[self.KEY] != key:
                node_ref = node_ref.next
            if node_ref == None:
                raise Exception
            return node_ref.val[self.VAL]
        else:
            raise Exception

    # I feel like there is probably an optimization here to instead of completely getting rid
    # of the node in the list and allowing the GC to deal with it we instead reuse it, and replace the values in it.
    def delete(self, key):
        hash_v = hash(key)
        index = hash_v % self.capacity
        if self.data[index] != self.EMPTY_NODE:
            node_ref = self.data[index]
            prev_ref = None
            while node_ref != None and node_ref.val[self.KEY] != key:
                prev_ref = node_ref
                node_ref = node_ref.next
            if node_ref == None:
                raise Exception

            # The node we are looking for is the first one
            if prev_ref == None:
                self.data[index] = node_ref.next if node_ref.next else ListNode()
                return
            prev_ref.next = node_ref.next
        else:
            raise Exception




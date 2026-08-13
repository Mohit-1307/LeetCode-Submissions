class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_last(self):
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.minFreq = 0
        self.keyMap = {}
        self.freqMap = defaultdict(DLL)

    def update(self, node):
        freq = node.freq
        self.freqMap[freq].remove(node)

        if freq == self.minFreq and self.freqMap[freq].size == 0:
            self.minFreq += 1

        node.freq += 1
        self.freqMap[node.freq].add_front(node)

    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1

        node = self.keyMap[key]
        self.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.keyMap:
            node = self.keyMap[key]
            node.val = value
            self.update(node)
            return

        if len(self.keyMap) == self.cap:
            node = self.freqMap[self.minFreq].remove_last()
            del self.keyMap[node.key]

        node = Node(key, value)
        self.keyMap[key] = node
        self.freqMap[1].add_front(node)
        self.minFreq = 1
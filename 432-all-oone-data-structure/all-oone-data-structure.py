class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.key_to_node = {}

    def _insert_after(self, prev_node, new_node):
        new_node.next = prev_node.next
        new_node.prev = prev_node

        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.key_to_node:

            if self.head.next != self.tail and self.head.next.count == 1:
                node = self.head.next
            else:
                node = Node(1)
                self._insert_after(self.head, node)

            node.keys.add(key)
            self.key_to_node[key] = node
            return

        cur = self.key_to_node[key]

        if cur.next != self.tail and cur.next.count == cur.count + 1:
            nxt = cur.next
        else:
            nxt = Node(cur.count + 1)
            self._insert_after(cur, nxt)

        nxt.keys.add(key)
        self.key_to_node[key] = nxt

        cur.keys.remove(key)

        if not cur.keys:
            self._remove_node(cur)

    def dec(self, key: str) -> None:
        cur = self.key_to_node[key]

        if cur.count == 1:
            del self.key_to_node[key]
        else:
            if cur.prev != self.head and cur.prev.count == cur.count - 1:
                prev_node = cur.prev
            else:
                prev_node = Node(cur.count - 1)
                self._insert_after(cur.prev, prev_node)

            prev_node.keys.add(key)
            self.key_to_node[key] = prev_node

        cur.keys.remove(key)

        if not cur.keys:
            self._remove_node(cur)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""

        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""

        return next(iter(self.head.next.keys))
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
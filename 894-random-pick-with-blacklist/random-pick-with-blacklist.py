class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.size = n - len(blacklist)

        black = set(blacklist)

        self.mp = {}

        last = n - 1

        for b in blacklist:
            if b >= self.size:
                continue

            while last in black:
                last -= 1

            self.mp[b] = last
            last -= 1

    def pick(self) -> int:
        x = random.randint(0, self.size - 1)
        return self.mp.get(x, x)
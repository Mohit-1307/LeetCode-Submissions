class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums[:]
        self.bit = [0] * (self.n + 1)

        for i, x in enumerate(nums):
            self.add(i + 1, x)

    def add(self, idx, delta):
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def prefix(self, idx):
        s = 0
        idx += 1          # convert to 1-based index
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s

    def update(self, index, val):
        delta = val - self.nums[index]
        self.nums[index] = val
        self.add(index + 1, delta)

    def sumRange(self, left, right):
        return self.prefix(right) - self.prefix(left - 1)
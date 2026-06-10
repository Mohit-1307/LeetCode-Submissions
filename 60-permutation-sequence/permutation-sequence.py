class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # factorials
        fact = [1] * n
        for i in range(1, n):
            fact[i] = fact[i - 1] * i

        nums = [str(i) for i in range(1, n + 1)]

        k -= 1  # zero-based
        ans = []

        for i in range(n, 0, -1):
            block_size = fact[i - 1]

            idx = k // block_size
            ans.append(nums.pop(idx))

            k %= block_size

        return "".join(ans)
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        a %= MOD

        ans = 1

        for digit in b:
            ans = pow(ans, 10, MOD) * pow(a, digit, MOD)
            ans %= MOD

        return ans
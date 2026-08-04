class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MOD = 10**9 + 7

        end0 = 0
        end1 = 0
        hasZero = False

        for ch in binary:
            if ch == '1':
                end1 = (end0 + end1 + 1) % MOD
            else:
                hasZero = True
                end0 = (end0 + end1) % MOD

        return (end0 + end1 + hasZero) % MOD
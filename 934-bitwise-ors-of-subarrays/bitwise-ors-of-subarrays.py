class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        cur = set()      # ORs of subarrays ending at current index
        ans = set()

        for x in arr:
            cur = {x} | {v | x for v in cur}
            ans |= cur

        return len(ans)
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(freq % 2 == 0 for freq in Counter(nums).values())
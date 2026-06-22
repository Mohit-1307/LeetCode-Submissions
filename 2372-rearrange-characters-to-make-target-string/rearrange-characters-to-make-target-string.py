class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        fs = Counter(s)
        ft = Counter(target)

        return min(fs[ch] // ft[ch] for ch in ft)
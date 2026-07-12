class Solution:
    def equalFrequency(self, word: str) -> bool:
        n = len(word)

        for i in range(n):
            freq = Counter(word[:i] + word[i + 1:])
            vals = list(freq.values())

            if len(set(vals)) == 1:
                return True

        return False
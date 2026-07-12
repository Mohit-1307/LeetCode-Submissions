class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = [0] * 26

        for ch in words[0]:
            freq[ord(ch) - ord('a')] += 1

        for word in words[1:]:
            curr = [0] * 26
            for ch in word:
                curr[ord(ch) - ord('a')] += 1

            for i in range(26):
                freq[i] = min(freq[i], curr[i])

        ans = []
        for i in range(26):
            ans.extend([chr(i + ord('a'))] * freq[i])

        return ans
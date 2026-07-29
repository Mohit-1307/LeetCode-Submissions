class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        half = [0] * 26
        mid = ""

        for ch, f in freq.items():
            idx = ord(ch) - ord('a')
            half[idx] = f // 2
            if f & 1:
                mid = ch

        m = sum(half)

        # Total number of distinct half permutations.
        ways = 1
        rem = m
        for c in half:
            if c:
                ways *= comb(rem, c)
                rem -= c

        if ways < k:
            return ""

        ans = []
        rem = m

        while rem:
            for i in range(26):
                if half[i] == 0:
                    continue

                # Number of completions if this character is chosen now.
                cnt = ways * half[i] // rem

                if k > cnt:
                    k -= cnt
                else:
                    ans.append(chr(i + ord('a')))
                    ways = cnt
                    half[i] -= 1
                    rem -= 1
                    break

        left = "".join(ans)
        return left + mid + left[::-1]
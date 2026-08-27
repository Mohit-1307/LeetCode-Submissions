class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Frequency of characters in s
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # Match target from left to right as long as possible.
        matched = []

        for i in range(n):
            x = ord(target[i]) - ord('a')

            if cnt[x] > 0:
                cnt[x] -= 1
                matched.append(x)
                continue

            # We cannot match target[i].
            # Try making the first difference at i or earlier.
            for j in range(i, -1, -1):

                # If j < i, restore the character previously
                # used at position j.
                if j < i:
                    cnt[matched[j]] += 1

                t = ord(target[j]) - ord('a')

                # Pick the smallest available character > target[j]
                for c in range(t + 1, 26):
                    if cnt[c] > 0:
                        cnt[c] -= 1

                        # target[:j] is already fixed.
                        ans = target[:j] + chr(c + ord('a'))

                        # Remaining characters in sorted order.
                        for k in range(26):
                            ans += chr(k + ord('a')) * cnt[k]

                        return ans

            return ""

        # We matched target completely.
        # Therefore target itself is a permutation of s.
        # Find the next lexicographically greater permutation.

        for j in range(n - 1, -1, -1):
            # Restore target[j]
            cnt[matched[j]] += 1

            t = matched[j]

            # Find smallest available character > target[j]
            for c in range(t + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1

                    ans = target[:j] + chr(c + ord('a'))

                    # Smallest possible suffix
                    for k in range(26):
                        ans += chr(k + ord('a')) * cnt[k]

                    return ans

        return ""
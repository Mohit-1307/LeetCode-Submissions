from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        half = n // 2

        cnt = Counter(s)

        # A palindrome is possible only if at most one
        # character has an odd frequency.
        if sum(v % 2 for v in cnt.values()) > 1:
            return ""

        # Characters available in the first half.
        freq = [0] * 26
        for i in range(26):
            freq[i] = cnt[chr(97 + i)] // 2

        mid = ""
        if n % 2:
            for c in cnt:
                if cnt[c] % 2:
                    mid = c
                    break

        # We only need to construct the first half.
        # target comparison is determined from left to right.
        ans = []

        def build_palindrome(left):
            left_str = ''.join(chr(x + 97) for x in left)
            return left_str + mid + left_str[::-1]

        def dfs(pos, greater):
            # All positions of the left half are filled.
            if pos == half:
                if greater:
                    return build_palindrome(ans)

                # The left half equals target's left half.
                # Need to compare the complete palindrome because
                # the middle/right half may make it greater.
                candidate = build_palindrome(ans)
                if candidate > target:
                    return candidate

                return None

            target_char = ord(target[pos]) - 97

            # If we are already greater, choose the smallest
            # available character.
            if greater:
                for c in range(26):
                    if freq[c] == 0:
                        continue

                    freq[c] -= 1
                    ans.append(c)

                    res = dfs(pos + 1, True)
                    if res is not None:
                        return res

                    ans.pop()
                    freq[c] += 1

                return None

            # We are still equal to target's prefix.
            #
            # Try characters from smallest to largest.
            # This guarantees the first solution is lexicographically
            # smallest.
            for c in range(26):
                if freq[c] == 0:
                    continue

                if c < target_char:
                    continue

                freq[c] -= 1
                ans.append(c)

                if c == target_char:
                    res = dfs(pos + 1, False)
                else:
                    res = dfs(pos + 1, True)

                if res is not None:
                    return res

                ans.pop()
                freq[c] += 1

            return None

        result = dfs(0, False)
        return result if result is not None else ""
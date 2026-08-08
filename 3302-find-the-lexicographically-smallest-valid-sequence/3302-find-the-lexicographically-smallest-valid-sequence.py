class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        # suf[i] = earliest index in word1 from which word2[i:] can be matched
        suf = [-1] * (m + 1)
        suf[m] = n

        p = n - 1
        for i in range(m - 1, -1, -1):
            while p >= 0 and word1[p] != word2[i]:
                p -= 1
            if p < 0:
                break
            suf[i] = p
            p -= 1

        ans = []
        i = 0
        used = False

        for j in range(m):
            while i < n:
                # normal match
                if word1[i] == word2[j]:
                    ans.append(i)
                    i += 1
                    break

                # use one modification
                if (not used) and (j == m - 1 or (suf[j + 1] != -1 and suf[j + 1] > i)):
                    used = True
                    ans.append(i)
                    i += 1
                    break

                i += 1
            else:
                return []

        return ans
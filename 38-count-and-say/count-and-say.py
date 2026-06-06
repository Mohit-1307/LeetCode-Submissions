class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"

        for _ in range(n - 1):
            curr = []
            count = 1

            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    curr.append(str(count))
                    curr.append(s[i - 1])
                    count = 1

            curr.append(str(count))
            curr.append(s[-1])

            s = "".join(curr)

        return s
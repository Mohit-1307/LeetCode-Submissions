class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []

        def dfs(i, cur):
            if i == n:
                ans.append("".join(cur))
                return

            # always place 1
            cur.append('1')
            dfs(i + 1, cur)
            cur.pop()

            # place 0 only if previous char isn't 0
            if not cur or cur[-1] != '0':
                cur.append('0')
                dfs(i + 1, cur)
                cur.pop()

        dfs(0, [])
        return ans
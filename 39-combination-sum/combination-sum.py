class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def dfs(start: int, remaining: int, path: List[int]) -> None:
            if remaining == 0:
                ans.append(path[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])

                # Reuse same element
                dfs(i, remaining - candidates[i], path)

                path.pop()

        dfs(0, target, [])
        return ans
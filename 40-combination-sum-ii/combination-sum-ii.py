class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def dfs(start: int, target: int, path: List[int]) -> None:
            if target == 0:
                ans.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(i + 1, target - candidates[i], path)
                path.pop()

        dfs(0, target, [])
        return ans
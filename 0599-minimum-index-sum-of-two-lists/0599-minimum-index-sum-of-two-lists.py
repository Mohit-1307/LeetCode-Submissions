class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        index_map = {s: i for i, s in enumerate(list1)}

        min_sum = float('inf')
        ans = []

        for j, s in enumerate(list2):
            if s in index_map:
                index_sum = index_map[s] + j

                if index_sum < min_sum:
                    min_sum = index_sum
                    ans = [s]

                elif index_sum == min_sum:
                    ans.append(s)

        return ans
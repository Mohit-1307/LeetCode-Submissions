class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index, current):

            # Base case
            if index == len(digits):
                result.append(current)
                return

            # Get letters for current digit
            letters = phone[digits[index]]

            # Try every possible letter
            for ch in letters:
                backtrack(index + 1, current + ch)

        backtrack(0, "")

        return result
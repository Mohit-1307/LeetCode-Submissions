class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:

            # Opening bracket
            if ch in "([{":
                stack.append(ch)

            # Closing bracket
            else:

                # Stack empty OR mismatch
                if not stack or stack[-1] != mapping[ch]:
                    return False

                stack.pop()

        # Valid only if stack becomes empty
        return len(stack) == 0
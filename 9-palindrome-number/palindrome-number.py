class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindrome
        if x < 0:
            return False

        # Numbers ending with 0 cannot be palindrome
        # except 0 itself
        if x % 10 == 0 and x != 0:
            return False

        reversed_half = 0

        while x > reversed_half:

            digit = x % 10

            reversed_half = reversed_half * 10 + digit

            x //= 10

        # Even length:
        # x == reversed_half

        # Odd length:
        # x == reversed_half // 10

        return x == reversed_half or x == reversed_half // 10
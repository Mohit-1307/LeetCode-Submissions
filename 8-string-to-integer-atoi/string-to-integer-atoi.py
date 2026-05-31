class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)

        # Step 1: Skip whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Sign handling
        sign = 1

        if i < n and (s[i] == '+' or s[i] == '-'):

            if s[i] == '-':
                sign = -1

            i += 1

        # Step 3: Convert digits
        result = 0

        while i < n and s[i].isdigit():

            digit = int(s[i])

            # Step 4: Overflow check
            if result > INT_MAX // 10:
                return INT_MAX if sign == 1 else INT_MIN

            if result == INT_MAX // 10:

                if sign == 1 and digit > 7:
                    return INT_MAX

                if sign == -1 and digit > 8:
                    return INT_MIN

            result = result * 10 + digit

            i += 1

        return sign * result
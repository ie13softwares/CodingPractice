# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output:  321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Reversed Number
        rx = 0
        negative = x < 0
        x = abs(x)
        while x != 0:
            rx = rx * 10 + x % 10
            x = x // 10

        if x > 2**32 - 1:
            return 0

        return rx if not negative else -rx


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(123))

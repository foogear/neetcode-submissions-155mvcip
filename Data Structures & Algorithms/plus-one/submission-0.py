class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1

        for i in reversed(range(len(digits))):

            if digits[i] + 1 >= 10:
                carry = 1
                digits[i] = 0
            else:
                carry = 0
                digits[i] += 1
                break

        if carry:
            return [1] + digits

        return digits
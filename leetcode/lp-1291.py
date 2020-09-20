# 1291. Sequential Digits
# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
#
# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
#
#
#
# Example 1:
#
# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:
#
# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        digits = '123456789'
        nl,nh= len(str(low)),len(str(high))

        for i in range(nl,nh+1):
            for j in range(0,10-i):
                num = int(digits[j:j+i])

                if low <= num <= high:
                    result.append(num)

        return result

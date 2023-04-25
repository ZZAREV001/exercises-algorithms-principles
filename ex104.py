# Roman numerals to decimal
class Solution:
    @staticmethod
    def romanToDef(s):  # we need a hashmap data structure to keep track of Roman legend number
        romanNumerals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        prev = 0
        sum = 0
        for i in s[::-1]:
            curr = romanNumerals[i]
            # remark: Python can't do ternaries like in Java
            if prev > curr:
                sum -= curr
            else:
                sum += curr
            prev = curr
        return sum


n = 'MCMIV'
print(Solution().romanToDef(n))
# expect 1904


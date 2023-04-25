# Simple calculator (avoid one big function,  divide in 2 sub-problems with 2 small functions)
class Solution(object):

    def __eval_helper(self, expression, index):     # __ makes private this method
        op = '+'          # start an index at 0 and while this index is less than the expression parameter, we get the character for each index in the string:
        result = 0        # initialize the result at 0
        while index < len(expression):
            char = expression[index]
            if char in ('+', '-'):
                op = char
            else:
                if char.isdigit():
                    value = int(char)  # convert the char here in integer format
                elif char == '(':  # recurse here if char in the string is a parenthesis: return the value and the parenthesis
                    (value, index) = self.__eval_helper(expression, index + 1)
                if op == '+':
                    result += value
                if op == '-':
                    result -= value
        index += 1
        return (result, index)

    def eval(self, expression):
        return self.__eval_helper(expression, 0)[0]


print(Solution().eval('- (3 + (2 - 1) )'))
print(Solution().eval('3 + 2 + 7'))

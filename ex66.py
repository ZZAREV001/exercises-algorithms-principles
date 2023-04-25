# First recurring character of a string
class Solution:

    def first_recurring_character(cls):
        seen = set()

        for c in cls:
            if c in seen:
                return c
            seen.add(c)

        return None


print(Solution.first_recurring_character('qwertty'))
# expect value 't'
print(Solution.first_recurring_character('qwerty'))
# expect None
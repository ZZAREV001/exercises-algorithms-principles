# Character mapping
class Solution(object):
    @staticmethod
    def has_character_map(string1, string2):
        if len(string1) != len(string2):       # conditional: compare number of components in each strings
            return False

        chars = {}           # create an empty hashmap
        for i in range(len(string1)):     # iterate through the interval of components of string1
            if string1[i] not in chars:
                chars[string1[i]] = string2[i]
            else:
                if chars[string1[i]] != string2[i]:
                    return False
        return True


print(Solution().has_character_map('abc', 'def'))
# expect true
print(Solution().has_character_map('aac', 'def'))
# expect false
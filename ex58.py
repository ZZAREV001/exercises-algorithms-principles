# Longest substring without repeating characters
def lengthOfLongestSubstring(str):
    letter_position = {}
    start = -1
    end = 0
    max_length = 0

    while end < len(str):
        c = str[end]
        if c in letter_position:
            start = max(start, letter_position[c])

        max_length = max(max_length, end - start)

        letter_position[c] = end
        end += 1
    return max_length


print(lengthOfLongestSubstring('aabcbbeac'))

# def lengthOfLongestSubstring02(self, s):
    # if not s:
       # return 0
#
    # visited = defaultdict(int)
    # ans, start =0, 0
    # for end, ch in enumerate(s):
          # if ch in visited:
              # start = max(start, visited[ch] + 1)
#
      # visited[ch] = end
      # ans = max(ans, end -start +1)
#
     # return ans

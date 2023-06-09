# Circle of chained words (DFS problem)
import collections


def is_cycle_dfs(symbol, current_word, start_word, length, visited):
    if length == 1:
        return start_word[0] == current_word[-1]    # add 0 to access first letter of starting word and add -1 to access last character of the current word. If not, string is never checked.

    visited.add(current_word)
    for neighbor in symbol[current_word[-1]]:
        if neighbor not in visited:
            return is_cycle_dfs(symbol, neighbor, start_word, length - 1, visited)
    visited.remove(current_word)
    return False

def chainedWords(words):
    symbol = collections.defaultdict(list)
    for word in words:
        symbol[word[0]].append(word)

    return is_cycle_dfs(symbol, words[0], words[0], len(words), set())


print(chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))    # expected true
print(chainedWords(['apple', 'eggs', 'snack', 'karat', 'tunax']))   # expected false
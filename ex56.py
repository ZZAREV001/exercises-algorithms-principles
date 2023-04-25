# Phone numbers
letterMaps = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: []
}

validWords = ['dog', 'fish', 'cat', 'fog']


def makeWordsHelper(digits, letters):
    if not digits:
        word = ''.join(letters)
        if word in validWords:
            return [word]
        return []

    results = []
    chars = letterMaps[digits[0]]
    for char in chars:
        results += makeWordsHelper(digits[1:], letters + [char])
    return results


def makeWords(phone):
    digits = []
    for digit in phone:
        digits.append(int(digit))
    return makeWordsHelper(digits, [])


print(makeWords('364'))